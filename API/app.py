from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="LangchainSErver",
    version = "1.0",
    description="A Simple API Server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
model=ChatOpenAI()

llm=Ollama(model="llama2")

prompt1=ChatPromptTemplate.from_template("write me an essay about {topic} with 20 words")
prompt2=ChatPromptTemplate.from_template("write me an poem about {topic} for 5 year child")


add_routes(
    app,
    prompt1|model,
    path="/essay"
)
add_routes(
    app,
    prompt2|llm,
    path="/poem"
)



if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=7000)







