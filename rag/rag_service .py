import chromadb
from chromadb.utils import embedding_functions
from core.config import settings

client = chromadb.PersistentClient(path=settings.CHROMA_DB_DIR)
embedding = embedding_functions.DefaultEmbeddingFunction()

collection = client.get_or_create_collection(
    name="lesson_kb",
    embedding_function=embedding
)

class RAGService:
    @staticmethod
    def add_document(doc_id: str, content: str, metadata: dict = None):
        collection.add(
            documents=[content],
            metadatas=[metadata or {}],
            ids=[doc_id]
        )

    @staticmethod
    def search(query: str, top_k=3):
        results = collection.query(
            query_texts=[query],
            n_results=top_k
        )
        return results

    @staticmethod
    def clear():
        global collection
        client.delete_collection("lesson_kb")
        collection = client.get_or_create_collection("lesson_kb", embedding_function=embedding)