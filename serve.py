from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv
from langserve import add_routes
load_dotenv

groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model = "llama-3.2-1b-preview", groq_api_key = groq_api_key)

generic_template = "translate the following into {language}:"

prompt = ChatPromptTemplate.from_messages(
    [("system",generic_template),("user","{text}")]
)
parser = StrOutputParser()

chain = prompt|model|parser

app = FastAPI(title = "langchain server",
              version = "1.0",
              description = "a simple API server using Langchain runnable interfaces")

add_routes(
    app,
    chain,
    path = "/chain"

)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host = "localhost",port = 8000)