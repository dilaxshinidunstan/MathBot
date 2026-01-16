from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings  # CORRECT IMPORT
import os

PDF_PATH = "data/math_books/grade10_maths.pdf"
VECTOR_DB_PATH = "vectorstore/"

def ingest_pdf():
    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  # Fast local model

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(VECTOR_DB_PATH)

    print("Math knowledge base created successfully.")

if __name__ == "__main__":
    ingest_pdf()