import requests
import streamlit as st


def get_gemini_response_essay(input_text):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={"input":{"topic": input_text}}
    )
    return response.json()['output']['content']



def get_gemini_response_poem(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={"input":{"topic": input_text}}
    )
    return response.json()['output']['content']

st.title("Langchain Gemini API Client")
input_text1 = st.text_input("Enter a topic for the essay")
input_text2 = st.text_input("Enter a topic for the poem") 

if input_text1:
    essay_response = get_gemini_response_essay(input_text1)
    st.header("Essay:")
    st.write(essay_response)

if input_text2:
    poem_response = get_gemini_response_poem(input_text2)
    st.header("Poem:")
    st.write(poem_response) 