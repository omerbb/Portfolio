import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv, GraphSAGE, GATConv
from torch_geometric.data import Data
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Veriyi yükleyelim
with open('dsmv.json', 'r') as f:
    data = json.load(f)

# DSM bozuklukları ve semptomlarını çıkaralım
disorders = []
categories = {}
diagnostic_features = []

for category in data['data']:
    main_category = category['category_name']
    categories[category['category_id']] = main_category
    for subcategory in category.get('subcategories', []):
        subcategory_name = subcategory['category_name']
        for disorder in subcategory['disorders']:
            diagnostic_criteria = [criterion['dco_body'] for criterion in disorder.get('diagnostic_criteria', {}).get('criteria', [])]
            diagnostic_features.append(" ".join(diagnostic_criteria))  # Semptomları birleştiriyoruz
            disorders.append({
                'id': disorder['disorder_id'],
                'name': disorder['disorder_name'],
                'category': main_category,
                'diagnostic_criteria': diagnostic_criteria
            })

# 1. TF-IDF ile benzerlik hesaplama
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(diagnostic_features)
tfidf_similarity = cosine_similarity(tfidf_matrix)

# 2. Kenarları (edges) oluşturalım ve edge'leri olan node'ları tespit edelim
edges = []
similarity_weights = []
nodes_with_edges = set()  # Edge'leri olan node'ları kaydedeceğiz
threshold = 0.2  # Benzerlik için eşik değeri
for i in range(len(disorders)):
    for j in range(i+1, len(disorders)):
        if tfidf_similarity[i][j] > threshold:
            edges.append((i, j))
            similarity_weights.append(tfidf_similarity[i][j])  # Kenarların benzerliklerine göre uzunluk
            nodes_with_edges.add(i)  # Edge'e sahip olan node'ları kaydet
            nodes_with_edges.add(j)

# 3. Düğümleri yeniden indeksleyelim
nodes_with_edges = list(nodes_with_edges)
node_map = {old_index: new_index for new_index, old_index in enumerate(nodes_with_edges)}

# Filtrelenmiş edge'ler için yeni indeksler
filtered_edges = [(node_map[i], node_map[j]) for i, j in edges if i in node_map and j in node_map]

# GNN modelini tanımlayalım
class GNNModel(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(GNNModel, self).__init__()
        self.conv1 = GCNConv(input_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, output_dim)
        self.conv3 = GATConv(output_dim, output_dim)  # GAT katmanı eklendi

    def forward(self, data):
        x, edge_index, edge_weight = data.x, data.edge_index, data.edge_weight
        x = self.conv1(x, edge_index, edge_weight=edge_weight)
        x = x * torch.sigmoid(x)
        x = self.conv2(x, edge_index, edge_weight=edge_weight)
        x = x * torch.sigmoid(x)
        x = self.conv3(x, edge_index)  # GAT katmanı ekleniyor
        return F.softmax(x, dim=1)

# 4. Node ve edge özelliklerinin geliştirilmesi
node_features = tfidf_matrix.toarray()  # TF-IDF temsillerini düğüm özellikleri olarak kullanıyoruz
x = torch.tensor(node_features[nodes_with_edges], dtype=torch.float)  # Node özellikleri
edge_weights = torch.tensor(similarity_weights, dtype=torch.float)  # Kenar ağırlıkları
edge_index = torch.tensor(filtered_edges, dtype=torch.long).t().contiguous()

# Data objesini oluştur
data = Data(x=x, edge_index=edge_index, edge_weight=edge_weights)

# 5. Modeli eğitme
def train_model(data):
    model = GNNModel(input_dim=data.num_node_features, hidden_dim=64, output_dim=data.num_node_features)  # 32 boyutlu çıktı için
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    model.train()
    for epoch in range(500):
        optimizer.zero_grad()
        out = model(data)
        loss = F.mse_loss(out, data.x)  # Özellik rekonstrüksiyonu
        loss.backward()
        optimizer.step()
        print(f'Epoch {epoch+1}, Loss: {loss.item()}')
    
    return model

# GNN modelini eğit
model = train_model(data)

# 6. Düğüm embedding'lerini çıkaralım
model.eval()
with torch.no_grad():
    node_embeddings = model(data).numpy()

# 7. NetworkX Grafiği Hazırlama
G = nx.Graph()

# Düğümleri ekleyelim
for i, old_index in enumerate(nodes_with_edges):
    G.add_node(i, label=disorders[old_index]['name'], category=disorders[old_index]['category'])

# Kenarları ekleyelim
for edge, weight in zip(filtered_edges, similarity_weights):
    G.add_edge(edge[0], edge[1], weight=weight)

# 8. Matplotlib ile grafiği çizme
pos = nx.spring_layout(G, k=0.3)  # Düğümler için pozisyon belirleme

fig, ax = plt.subplots(figsize=(12, 12))

# Kenarları çiz
edge_colors = []
node_edge_color_map = {}
for edge in G.edges:
    node = edge[0]
    if node not in node_edge_color_map:
        node_edge_color_map[node] = np.random.rand(3,)
    edge_colors.append(node_edge_color_map[node])
line_collection = nx.draw_networkx_edges(G, pos, alpha=0.5, ax=ax, edge_color=edge_colors, width=1)

# Kenarların üzerine gelindiğinde kalınlaşması için etkileşimli hale getirme
def on_hover(event):
    if event.inaxes == ax:
        cont, ind = line_collection.contains(event)
        if cont:
            linewidths = [1] * len(G.edges)
            for i in ind['ind']:
                linewidths[i] = 3
            line_collection.set_linewidths(linewidths)
            fig.canvas.draw_idle()

fig.canvas.mpl_connect('motion_notify_event', on_hover)

# Düğümleri çiz
node_categories = [G.nodes[node]['category'] for node in G.nodes]
category_colors = {category: np.random.rand(3,) for category in categories.values()}
node_colors = [category_colors[category] for category in node_categories]
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=300, alpha=0.8, ax=ax)

# Scatter plot oluşturarak etkileşimli hale getirme
node_positions = np.array([pos[node] for node in G.nodes])
sc = ax.scatter(node_positions[:, 0], node_positions[:, 1], s=300, c=node_colors, alpha=0.8)

# Etiketleri hazırlama
annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    node_index = ind["ind"][0]
    text = G.nodes[node_index]['label']
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor(category_colors[G.nodes[node_index]['category']])
    annot.get_bbox_patch().set_alpha(1.0)

def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.title('DSM-5 Bozuklukları Arasındaki GNN Sonuçları')

# Sağ üstte nodeların renklerinin anlamlarını gösterme
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', label=category, markersize=10, markerfacecolor=color)
    for category, color in category_colors.items() if category in node_categories
]
ax.legend(handles=legend_elements, loc='upper right', fontsize='small')
plt.tight_layout()
plt.axis('off')
plt.show()

