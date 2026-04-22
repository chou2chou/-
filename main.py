from fastapi import FastAPI
from core.websocket import router as ws_router
from api.lesson import router as lesson_router
from api.db_test import router as db_test_router

app = FastAPI(title="面向听障学生的多模态教育智能体", version="1.0")

app.include_router(ws_router)
app.include_router(lesson_router)
app.include_router(db_test_router)

@app.get("/")
def root():
    return {"msg": "听障教育智能体后端运行成功"}