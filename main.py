import os 
import streamlit as st 
from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All,OpenAI
from openaiKey import openAIapikey

# PATH = '/Applications/gpt4all/bin/ggml-vicuna-7b-1.1-q4_2.bin'

os.environ['OPENAI_API_KEY'] = openAIapikey

# If u want to use any local free LLM model like GPT4All e.t.c
# llm = GPT4All(model=PATH, verbose=True)
llm = OpenAI(temperature=0.2, verbose=True)

prompt = PromptTemplate(input_variables=['question'], template="""
    write a complete detailed youtube script, tags and title for this context: {question}
    """)

llm_chain = LLMChain(prompt=prompt, llm=llm)

st.title('OpenAI based Youtube Script Creator')
st.info('You can also use local free LLMs')

prompt = st.text_input('Enter your video context here!!')

if prompt: 
    response = llm_chain.run(prompt)
    st.write(response)

