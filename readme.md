# Portfolio

## 1.1 Introduction

Welcome to my portfolio. This repository serves as a curated collection of my work, demonstrating a journey from foundational academic research to applied professional projects and deep-dive, from-scratch algorithm implementations. My goal is to showcase not just the final products, but also the process of bridging theory and practice across data science, machine learning, and software engineering.

The projects here span a wide range of domains—from robotics and LLM integration to bioinformatics and quantitative analysis—all unified by a first-principles approach to problem-solving.

### How This README is Organized

To make navigation intuitive, this document is structured thematically. It begins with a comprehensive **Tech Stack** summary, followed by sections that group projects by their context:

*   **Section 2: Academic Projects:** Highlights my published, grant-funded research and formal internship work.
*   **Section 3: Professional Projects:** Showcases my contributions in a commercial setting, focusing on tool development and production-level workflows.
*   **Sections 4-6: From-Scratch Implementations & Explorations:** Details my personal projects where I build algorithms and simulations from the ground up to solidify my understanding of core concepts in control systems, GNNs, and signal processing.
*   **Section 7: Community Workshops:** Features materials from data-science workshops I've led, demonstrating my ability to communicate complex topics clearly.

### How This Repository is Organized

The repository's directory structure directly mirrors the sections in this README. For every project discussed, you can find the corresponding source code, notebooks, and assets in the numbered folder of the same name. For instance, the code for the projects detailed in *Section 5: Graph Neural Network (GNN) Explorations* is located in the `5. Graph Neural Network (GNN) Explorations/` directory.

Thank you for visiting. I invite you to explore the projects that interest you most.

## 1.2 Tech Stack Used in This Portfolio


#### **Programming Languages**

*   **Python:** The primary language used across a wide range of projects, from machine learning and data science to web applications and hardware control.
*   **C#:** Used for desktop application development with the .NET framework, specifically for the Electrical-Engineering Simulation Suite.
*   **Java:** Mentioned for a client application consuming a Python REST API, demonstrating cross-language integration.

#### **Data Science, Machine Learning & AI**

*   **Core Libraries:**
    *   **NumPy:** For numerical operations and scientific computing.
    *   **Pandas:** For data manipulation and analysis (implied in data cleaning workshop).
    *   **Matplotlib:** For creating static, animated, and interactive visualizations.
    *   **Scikit-learn:** Utilized for machine learning tasks, including TF-IDF vectorization and cosine similarity.
*   **Deep Learning & GNNs:**
    *   **PyTorch:** The main deep learning framework used.
    *   **PyTorch Geometric:** For implementing Graph Neural Networks (GCNConv, GATConv).
*   **Natural Language Processing (LLP):**
    *   **Google Generative AI (Gemini):** Used for the LLM-driven chatbot and code generator.
*   **Bio-Signal Processing:**
    *   **MNE:** For exploring, visualizing, and analyzing EEG data.
*   **Other Specialized Libraries:**
    *   **NetworkX:** For the creation, manipulation, and study of complex networks.

#### **Web Development & APIs**

*   **Frameworks:**
    *   **Streamlit:** For building and deploying the interactive web-based UI for the Acrome SMD Chatbot.
    *   **Flask:** Mentioned for creating a REST API to serve a machine learning model.
*   **Web Scraping:**
    *   **BeautifulSoup:** Mentioned for parsing HTML and XML documents.
    *   **Requests:** For making HTTP requests.

#### **DevOps, CI/CD & Tooling**

*   **Containerization:**
    *   **Docker & Docker Compose:** Used to containerize the Python chatbot application for easy deployment and scalability.
*   **Continuous Integration/Continuous Deployment (CI/CD):**
    *   **GitHub Actions:** For automating Python package testing, linting, and publishing to PyPI.
*   **Code Quality & Testing:**
    *   **Flake8:** For linting and enforcing style consistency in Python code.
    *   **Pytest & Unittest:** For writing and running automated tests.
*   **Package Management & Publishing:**
    *   **Pip:** The standard package manager for Python.
    *   **Setuptools:** For packaging Python projects.
    *   **PyPI & TestPyPI:** Platforms for distributing Python packages.

#### **Desktop & Hardware**

*   **C#/.NET:**
    *   **Windows Forms:** For building the GUI of the Electrical-Engineering Simulation Suite.
    *   **Visual Studio:** As the primary IDE for C# development.
*   **Hardware Interfacing (Python):**
    *   **PySerial:** For serial communication with hardware devices like the Acrome Smart Motor Drivers.
    *   **stm32loader:** For interacting with STM32 microcontrollers.
*   **Utilities:**
    *   **Colorama & Tabulate:** For creating formatted and colored command-line output.

---

## 2. Academic Projects


### 2.1 Bridging Genetic Algorithms and Gradient‑Based Learning in the *Chrome Dinosaur* Game

![Image](https://github.com/user-attachments/assets/e5706a3d-950e-4d7a-9cad-9200e63925ac)

**Context.** This IEEE‑published( DOI: [10.1109/ICHORA65333.2025.11017263](https://ieeexplore.ieee.org/document/11017263) ) study (TÜBİTAK‑2209/A funded) explores how to train an agent when no ground‑truth dataset exists: evolve a controller **with a Genetic Algorithm (GA)** to *create* data, then fine‑tune a Multi‑Layer Perceptron (MLP) **with gradient descent** on that data.

**Methodology & findings.**

* **GA phase.** Populations of bias‑free MLPs (2 inputs × 1 hidden layer × 1 output) were evolved until one reached a score of 800, and every state–action pair along that run was logged as synthetic training data .
* **Gradient phase.** New MLPs were trained on this dataset; a single epoch was found sufficient—additional epochs caused over‑fitting and score collapse .
* **Architecture sweep.** A compact **\[2‑10‑1]** network with tanh activation achieved the highest mean score (\~2000) .
* **Robustness test.** When obstacle timing was randomised, scores dropped 40–70 %, yet all models still played acceptably, proving some generalisation .
* **Activation study.** Tanh dramatically out‑performed ReLU and sigmoid, whose agents failed to clear the first obstacle .

**Contribution.** The project shows that GA‑generated trajectories can bootstrap data‑hungry gradient learners, marrying evolutionary exploration with efficient convergence . This hybrid recipe promises faster training and lower compute budgets for other simulation‑heavy tasks.

https://github.com/user-attachments/assets/cf3e6973-ff1f-479d-a66d-54256c06b95a

https://github.com/user-attachments/assets/4aff33a4-a6db-412e-9197-d70a915a0589

---
### 2.2 Convoy Detection from Ground‑Radar Streams
**Context.** During my summer internship at **Ave Bilişim** I tackled a defence‑industry problem for an anonymous radar vendor: automatically flagging vehicles that travel **in convoy** across a sparse roadside‑radar network. Because no labelled data existed, the work is currently a **proof‑of‑concept** slated for future validation with traffic‑simulation data.

**Methodology.**

1. **Spatial pre‑clustering.** Millions of raw detections are first grouped with a MiniBatch K‑Means elbow search to find the optimal number of spatial clusters before assigning each radar hit to a cluster .
2. **Temporal co‑occurrence trigger.** For every “reference” plate, the algorithm scans a ± 10 min window at each sensor to collect plates that pass the same sensor in that window, building a candidate convoy set .
3. **Path‐vector analysis.** Start/finish coordinates for each vehicle are converted to vectors; relative angles and approach/leave status are computed to see whether trajectories are parallel, converging or diverging .
4. **Feature engineering.** Additional cues—number of shared spatial clusters, shared sensors and common road distance—are extracted for every pair .
5. **Heuristic scoring & ranking.** A Gaussian‑weighted formula combines all features and ranks the most likely convoy members; weights are deliberately hand‑set and will later be learned from labelled data .

**Outcome & next steps.** The pipeline successfully isolated four plausible convoy plates in a 5 000+ row slice of simulated data, demonstrating end‑to‑end feasibility. Future work includes (i) generating synthetic but physics‑based traffic to tune the weighting scheme and (ii) integrating the model into a streaming environment.

---

These two projects showcase my ability to (a) design full analytics pipelines under real‑world data constraints and (b) blend optimisation paradigms to overcome data scarcity—skills I continue to refine through ongoing research and open‑source contributions.

## 3. Selected Professional Projects

### 3.1 LLM‑Driven Robot Control Toolkit

<img width="1066" height="403" alt="Image" src="https://github.com/user-attachments/assets/783ffe07-f3b1-4fd9-a2e6-12b29878b25b" />

**Context.** During my internship at **Acrome Robotics** I explored how Large Language Models (LLMs) can translate plain‑English commands into low‑level robot actions on Acrome’s Smart Motion Devices (SMD). The publicly documented PoC shows an LLM that parses intent, chooses the right SMD API call and sequences complex tasks such as pick‑and‑place or path following Acrome Robotics.

**Methodology.**

1. **Function‑calling schema.** Each natural‑language command is mapped to a JSON “skill call” understood by the robot firmware.
2. **Hierarchical planning.** The LLM first selects high‑level skills, then decomposes them into parameterised sub‑skills (grip, move‑to, release).
3. **Context retrieval.** Runtime sensor data and prior dialogue are injected into the prompt so the model can re‑plan on failures or clarify ambiguous goals.
4. **Safety envelope.** A rule‑based guard blocks prompts that move the robot outside its workspace or velocity limits.

For more info check out the blogposts I wrote about this project.
1. [AI Robotics Case - Controlling Robots with LLMs (Large Language Models)](https://acrome.net/post/controlling-robots-with-llms-large-language-models)
2. [Controlling Robots Built with SMD Using Flask API](https://acrome.net/post/controlling-robots-built-with-smd-using-flask-api)

---

### 3.2 Gemini‑Assisted SMD Library Code Generator
**Context.** To accelerate internal prototyping at **Acrome**, I “taught” Google’s Gemini API the company’s proprietary **Acrome‑SMD Python library** and wrapped it in a Streamlit chat UI. Colleagues could paste a task description and instantly receive runnable robot‑control code.

**Methodology & deliverables.**

1. **Repo‑to‑Text ingestion** of the SMD library to build a domain‑aware retrieval prompt.
2. **Streamlit front‑end** for live Q\&A and code suggestions .
3. **Dockerisation** so anyone could `docker compose up`, add their API key and start coding .

**Outcome.** A one‑day hack that turned into a routinely used internal tool, boosting developer velocity and inspiring the public article on robot‑LLM synergy referenced above.

---

### 3.3 Polyglot Prediction Microservice (Python Flask + Java Client)
**Context.** A self‑driven exercise to master **model‑to‑production** workflows: train a Decision‑Tree classifier in Python, expose it via a Flask REST API, and consume it from a Java application that batch‑posts CSV rows for inference.

**Pipeline.**

1. **Model training & serialisation.** Scikit‑learn pipeline pickled together with preprocessing.
2. **/predict endpoint.** Accepts JSON, checks whether the request already exists in the training set and returns both the cluster ID and predicted label if so .
3. **Java batch client.** Streams test rows, builds JSON payloads and prints HTTP codes and predictions to console .


---

### 3.4 EEGLAB Interactive Viewer (Python port)
**Context.** While assisting Assoc. Prof. Emine Elif Tülay, I automated the visual inspection of EEG datasets originally processed in MATLAB’s EEGLAB by writing a **Python/MNE** CLI that loads *.set* files and offers one‑command plots for raw signals, PSDs and ERPs.

**Features.**

* Automatic detection of **raw vs. epoch** data and interactive mode selection.
* On‑demand conversion of EEGLAB annotations into MNE epochs.
* Interactive loop—type *plot*, *psd*, *erp*, etc.—for rapid exploratory analysis .

**Impact.** Reduced a 10‑minute manual workflow to seconds.




---

These projects demonstrate my ability to (a) integrate modern ML/LLM techniques with real hardware and heterogeneous stacks, (b) productionise models through robust APIs, and (c) build developer‑friendly tools that shrink idea‑to‑prototype time—core strengths for a data‑science role in 2025.




## 4. Algorithm Implementations *from Scratch*

I regularly “re‑derive and re‑code” the algorithms I use so that the maths becomes muscle‑memory.
Below are three representative notebooks—each built **only with NumPy/Matplotlib**, no ML libraries—to deepen my intuition for optimisation, control and function approximation.

---
### 4.1 Adaptive PID‑NN Controller (from‑scratch implementation)

**Context.** To see how a neural network can *self‑tune* classical control, I wrote a minimal **PID‑NN hybrid** in pure NumPy/Matplotlib—no control libraries, just maths.

**Experiments & insight.**

* **Reference profiles.** The controller tracks a *step*, *ramp* and *sine* set‑point in separate runs, updating weights live.
* **Adaptation effect.** Because the NN learns $K_p, K_i, K_d$ on‑line, it suppresses overshoot that a fixed‑gain PID cannot when the plant gain $a_k$ drifts by 50 % over 60 s.
* **Implementation purity.** Entire loop—controller + plant + plots—fits in \~60 LOC; everything vectorised, so 500 simulation steps render instantly.


---

### 4.2 Radial Basis Function (RBF) Network
**Context.** To understand kernel methods beyond black‑box SVMs, I hand‑coded an RBF network for regression and classification.

**Key steps & findings.**

* **Centre selection.** Implemented **Mini‑Batch K‑Means** to pick prototypes; median inter‑centre distance sets the Gaussian $\sigma$.
* **Weight solve.** Closed‑form linear least‑squares via the Moore–Penrose pseudoinverse ($\boldsymbol{W}=(\Phi^{\top}\Phi)^{-1}\Phi^{\top}\boldsymbol{y}$).
* **Regularisation sweep.** Ridge penalty $\lambda\in[0,10^{-4}]$ plotted against RMSE; optimal $\lambda=10^{-3}$ on *Boston Housing*.


---

### 4.3 Real‑Time Particle Swarm Optimisation (PSO) Surface Minimiser

**Context.** To build geometric intuition for meta‑heuristic search, I coded a **50‑particle** PSO that hunts the minimum of the non‑convex surface

$$
f(x,y)=\arctan\!\bigl(x^{2}+y^{2}\bigr)+\sin(x+y),
$$

rendered live in 3‑D with Matplotlib.

https://github.com/user-attachments/assets/eb3be143-5e83-47ce-8a25-215db2d779c5

---

These **from‑scratch builds** show that I can move fluidly between mathematics and code, reason about stability/convexity, and validate ideas with hands‑on simulations—abilities that translate directly into rigorous, production‑ready data‑science work.


## 5. Graph Neural Network (GNN) Explorations

I often prototype *from scratch* to understand how GNN layers, edge attributes and layouts interact with human perception. Below are the two most illustrative experiments; both are accompanied by an **interactive video demo** in the portfolio.

---

### 5.1 DSM‑V Diagnostic‑Similarity Graph
**Context.** Curious how mental‑disorder taxonomies overlap, I scraped the public DSM‑V JSON (≈ 300 disorders) and asked: *Which diagnoses share the same clinical phrasing, and how would those relationships look in a graph latent‑space?*

**Pipeline.**

1. **Text‑to‑Graph.** TF‑IDF on every disorder’s diagnostic criteria → cosine‑similarity edges above 0.20. The raw string vectors double as initial node features.&#x20;
2. **Model stack.** Two **GCN** layers capture local homophily, a final **GAT** layer re‑weights edges with attention to highlight rare but informative links.&#x20;
3. **Self‑supervised training.** The network reconstructs its own TF‑IDF features (MSE loss) so no labels are needed, converging in < 500 epochs.&#x20;
4. **Fully interactive plot.** Hover‑to‑thicken edges plus tooltip labels were wired via Matplotlib events for intuitive exploration of comorbid clusters.&#x20;

**Outcome.** The embedding surfaced unexpected bridges (e.g. *Somatic Symptom Disorder* sitting between mood and anxiety clusters), sparking discussion with clinical friends and showcasing my ability to blend **NLP, GNNs and UX** for insight‑driven visuals.

https://github.com/user-attachments/assets/c1647917-dbe0-46b5-9e47-bf20b6822376

---

### 5.2 Hand‑Written Digit Similarity Network
**Context.** As a sanity check for graph construction choices, I applied the same edge‑inference logic to **MNIST**: connect average digit images whose cosine similarity exceeds 0.25.

**Highlights.**

* **Distance matrix analysis** reveals which digits confuse a nearest‑neighbour classifier (e.g. *3* vs *8*).&#x20;
* **Graph abstraction** condenses the 60 000‑image dataset into a ten‑node network whose edge weights encode visual closeness. Edge creation logic is compact and transparent.&#x20;
* **Interactive layout** uses *spring* forces so closely related digits literally pull together on screen, letting viewers *see* manifold relationships at a glance.

**Outcome.** Served as a control‑experiment verifying that my edge heuristics and layout tricks generalise beyond text data.

---

These GNN projects demonstrate my capacity to:

* translate arbitrary domains (psychiatry, image manifolds) into **graph structures**,
* choose and tune appropriate **message‑passing architectures**, and
* craft **interactive visualisations** that turn high‑dimensional maths into actionable intuition.


## 6. Electrical‑Engineering Simulation Suite *(concise roll‑up)*

> To deepen lecture concepts I rebuilt core **control, signal‑processing and power‑electronics** algorithms entirely in Python/NumPy and visualised every step. Rather than list eight separate notebooks, I merged them into two coherent mini‑platforms.

---

### 6.1 Interactive Control & Power Lab
*Notebooks merged:*
`discrete_control_design_with_prefilter_analysis`, `discrete_control_simulation_with_model_error_and_noise`, `s_to_z_plane_mapping_visualization`, `transformer_core_calculations`.

**What it does.**

* A single dashboard sweeps **continuous→discrete** conversions, tunes digital PID / pre‑filters, and stress‑tests controllers against plant‑parameter drift and measurement noise.
* A companion tab solves **transformer magnetics**—core flux, copper loss, optimum turns—letting sliders instantly update B‑H curves and efficiency maps.

**Skills evidenced.**

* **Control theory → code.** Bilinear (Tustin) mapping, root‑locus and closed‑form pole placement rendered live.
* **Numerical robustness.** Vectorised difference‑equation solvers hit 1 kHz real‑time on a laptop, enabling Monte‑Carlo runs for uncertainty analysis.
* **Pedagogy.** Hover‑tooltips explain each equation, turning dry formulas into an interactive lab.

---

### 6.2 Signals & Systems Playground
*Notebooks merged:*
`continuous_signal_transformations_and_delta_functions`, `discrete_signals_and_sine_components`, `dt_signal_and_lowpass_filtering`, `dtmf_generation_and_convolution`, `signal_convolution_and_fft_analysis`.

**What it does.**

* Generates canonical waveforms (steps, chirps, DTMF tones), applies **time/frequency shifts & scaling**, then pipes them through custom FIR/IIR designs.
* Side‑by‑side plots show raw vs. filtered signals, magnitude‑/phase‑responses and **FFT‑based convolution** accuracy.
* A “What‑If” panel toggles quantisation noise and zero‑order‑hold effects to visualise real‑hardware artefacts.

**Skills evidenced.**

* **DSP fundamentals.** Manual convolution/FFT equivalence, window‑method filter synthesis, and pole‑zero visualisation in both *s‑* and *z‑planes*.
* **Efficient vectorisation.** All transforms run in pure NumPy; even the dual‑tone DTMF demo synthesises dial‑pads at audio rate.
* **Educational UX.** Interactive cursors reveal energy at each harmonic, bridging math intuition with ear‑level perception.

---

**Impact.**
These sandboxes became my go‑to reference during exams and later helped classmates grasp abstract topics. More importantly, the habit of **re‑deriving algorithms before using libraries** feeds directly into my day‑to‑day data‑science work: I can debug numerical edge‑cases and reason about model behaviour from first principles rather than treating toolkits as black boxes.


## 7. Community Workshops — Web‑Scraping & Data‑Cleaning Mini‑Labs

### 7.1 CS2 Skin‑Market Scraper *(Web‑Scraping Crash‑Course)*
**Context.** While serving as **President of the University Data‑Science Society**, I ran a one‑evening lab on industrial‑scale web‑scraping. We reverse‑engineered the dynamic pricing tables of the *Counter‑Strike 2* skin marketplace and built a production‑ready scraper from scratch.

**Key ideas & take‑aways.**

1. **Stealth browser automation.** Participants learned to launch a hardened, bot‑undetectable Chrome instance with `undetected_chromedriver`, manage cookies and scrolling, then throttle requests to avoid IP bans.
2. **HTML parsing pipeline.** Raw page sources were streamed into **BeautifulSoup** where each “table‑overflow” `<div>` was parsed, normalised, and flushed into row‑based CSV chunks for incremental storage.
3. **Robustness patterns.** We injected retry logic, exponential back‑off and *in‑situ* HTML snapshots so students could debug missing elements live.
4. **Data product.** The final artefact was a CLI script that delivers a clean, daily‑refreshable price history for any weapon skin—perfect input for time‑series modelling or portfolio simulations.



---

### 7.2 Netflix Titles Cleanup *(Regex & Data‑Hygiene Sprint)*
**Context.** In a follow‑up workshop focused on **real‑world data munging**, I provided an intentionally “dirty” extract of Netflix title metadata (10 000 rows) together with an auxiliary survey log containing inconsistent names & dates.

**Workflow.**

* **Missing‑value diagnosis.** Students visualised holes in the dataframe with `missingno.matrix`, then prioritised fixes.
* **Regex‑powered parsing.** We wrote vectorised regular‑expressions to split compound *name–surname* fields and coerce free‑form dates (`"2022/02/20"`, `"01‑03‑2022"`, `"March 1st ‘22"`) into ISO‑8601 `Timestamp`s.
* **Type‑safe re‑engineering.** After schema enforcement (`pd.StringDtype`, nullable `Float64`), we rebuilt categorical columns to support one‑hot encoding downstream.
* **Quality gates.** A lightweight **pytest** suite asserted zero nulls in critical columns and < 1 % type‑coercion failures, instilling production‑mindset discipline.


---
### VBT Society Meeting
![Image](https://github.com/user-attachments/assets/0c41627a-502c-46f0-b67a-b7151de9c377)
![Image](https://github.com/user-attachments/assets/d2ae4c7a-c7be-4388-a17b-75e4d3b36bfb)
