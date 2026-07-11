from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm=llm)

#STATIC PROMPT
st.header("Reasearch Tool")
user_input = st.text_input("Enter your prompt: ")

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)





