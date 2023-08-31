from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

from llm import OpenAIModel

loader = TextLoader("journal_new.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(docs, embeddings, persist_directory="embeddings_log")

qa = RetrievalQA.from_llm(
    llm=OpenAI(model=OpenAIModel.CHEAP.value),
    retriever=db.as_retriever(),
)

query = input("> ")
print(qa.run(query))
