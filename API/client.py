import requests
import streamlit as st
import os
from dotenv import load_dotenv
import json
load_dotenv()
os.environ["Langchain_api_key"]= os.getenv("Langchain_api_key")
os.environ["Langchain_Tracing_V2"]="true"

def get_openai_response(input_text):
    response=requests.post("http://localhost:7000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:7000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

    ## streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))