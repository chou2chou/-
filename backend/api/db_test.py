from fastapi import APIRouter
from core.database import test_database

router = APIRouter()

@router.get("/db-test")
def test_db():
    ok = test_database()
    if ok:
        return {"status": "success", "msg": "数据库连接成功"}
    else:
        return {"status": "fail", "msg": "数据库连接失败"}