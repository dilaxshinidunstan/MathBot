from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

VECTOR_DB_PATH = "vectorstore/"

def retrieve_knowledge(query: str):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db.similarity_search(query, k=3)
