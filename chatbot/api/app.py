from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
#load env
load_dotenv()

os.environ['GEMINI_API_KEY'] = os.getenv('GEMINI_API_KEY')


app = FastAPI(
    title="Langchain Server ",
    description="A FastAPI application using Langchain with Gemini API",
    version="1.0.0"
)
# Initialize the Google Generative AI model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

#default route
add_routes(
    app,
    model,
    path="/gemini",
)
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words.")

add_routes(app,
           prompt1 | model,
           path='/essay')

add_routes(app,
           prompt2 | model,
           path='/poem') 

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
