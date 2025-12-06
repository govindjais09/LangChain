from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

#load env
load_dotenv()

#Enable tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"

#Prompt template
prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant that helps people responds to the user queries."),
    ("user","Question:{question}") 
])

#Streamlit app
st.title("Chatbot with Gemini-API& Langchain")
input_text=st.text_input("Search the topic you want:")

## gemini LLM
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
output_parser=StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))