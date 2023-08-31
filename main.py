from langchain import PromptTemplate, ConversationChain
from langchain.llms import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.callbacks import get_openai_callback
import os
import sys
import enum

from llm import OpenAIModel


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    print("No OPEN_API_KEY env var set", file=sys.stderr)

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = OpenAI(model_name=OpenAIModel.CHEAP.value, temperature=0.2)


def count_tokens(chain, query: str):
    with get_openai_callback() as cb:
        result = chain.run(query)
        print(f"> {cb.total_tokens} tokens: ${cb.total_cost}")
    return result


conversation_buf = ConversationChain(llm=llm, memory=ConversationBufferMemory())

while True:
    try:
        query = input("Q: ")
    except EOFError:
        break
    print(f"A: {count_tokens(conversation_buf, query)}")
