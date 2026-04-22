from fastapi import APIRouter, UploadFile, File
from models.models import LessonCreate
import chromadb
from chromadb.utils import embedding_functions
from core.config import settings

# -------------------- 直接把RAGService写在这里 --------------------
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
# -------------------------------------------------------------------

router = APIRouter(prefix="/api/lesson")

@router.post("/create")
def create_lesson(lesson: LessonCreate):
    return {
        "lesson_id": "lesson_1001",
        "name": lesson.name,
        "teacher": lesson.teacher,
        "msg": "创建成功"
    }

@router.post("/upload-ppt")
async def upload_ppt(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")
    RAGService.add_document(
        doc_id=file.filename,
        content=text,
        metadata={"type": "ppt"}
    )
    return {"msg": "PPT已存入知识库", "filename": file.filename}

@router.get("/note/{lesson_id}")
def get_lesson_note(lesson_id: str):
    return {
        "lesson_id": lesson_id,
        "subtitle": "实时字幕",
        "key_points": "重点知识点",
        "mind_map": "思维导图结构",
        "sign_script": "手语文案"
    }

@router.get("/rag/search")
def rag_search(query: str):
    res = RAGService.search(query)
    return {"query": query, "results": res}