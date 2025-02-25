from langchain.chains import LLMChain
#from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI

import os

# os.environ["OPENAI_API_KEY"] = "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"



template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = OpenAI()

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What is at the core of Popper's theory of science?"

response = llm_chain.run(question)
print(response)