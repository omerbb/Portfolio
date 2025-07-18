# -*- coding: utf-8 -*-
import streamlit as st
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path(".env"))

APIKEY=os.getenv("GOOGLE_API_KEY")

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))



st.set_page_config(page_title="Q&A Demo")
st.header("Acrome SMD Library Q&A Chatbot")
input=st.text_input("Input: ",key="input")

fw = open("cleandatafromsmdlibrary.txt", "r")
text = fw.read()

genai.configure(api_key=APIKEY)
model = genai.GenerativeModel('gemini-1.5-pro',system_instruction="You must answer the questions using the given github repo of acrome-smd python library")
chat = model.start_chat()
prompt=text+"   Considering the given github repo of acrome-smd library answer the question : '"+ input +"'"



#bu kodu yazarken hiçbir scan fonksiyonu kullanma lütfen. scan ve scan_modules kullanma

#elimdeki smd ye iki adet rgb modülü bağladım. smdnin idsi 13, modüllerin idsi 1 ve 3. bunları sırasıyla yeşil ve kırmızı olarak yak 1 saniye aralıklarla. birisi hep yeşil yanacakken diğeri hep kırmızı yanacak ama ikisi aynı anda yanmayacak 1 saniye aralıklarla yanan değişecek.  en hızlı şekilde başlayacak gibi hazırla

submit=st.button("Ask the question")

## If ask button is clicked
if submit:
    
    response=chat.send_message(prompt)
    st.subheader("Answer: ")
    st.write(response.text)
    
