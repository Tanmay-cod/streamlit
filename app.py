from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# creating my prompts

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant , please respond to the question"),
        ("user", "Question:{question}")
    ]
)

#frontend using streamlit

st.title("My GPT")
input_text = st.text_input("Ask your questions !")

#ollama and LLM model integration
llm = OllamaLLM(model = "gemma:latest")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text :
    st.write(chain.invoke({"question" : input_text}))    