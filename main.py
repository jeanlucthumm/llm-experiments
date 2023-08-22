from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
import os
import sys

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    print("No OPEN_API_KEY env var set", file=sys.stderr)

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = OpenAI()

llm_chain = LLMChain(prompt=prompt, llm=llm)
print(llm_chain.run(input("Enter question: ")))
