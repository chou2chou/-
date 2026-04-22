import pymysql
from pymysql.err import OperationalError
from core.config import settings

def get_db_connection():
    try:
        conn = pymysql.connect(
            host=settings.MYSQL_HOST,
            user=settings.MYSQL_USER,
            password=settings.MYSQL_PWD,
            database=settings.MYSQL_DB,
            cursorclass=pymysql.cursors.DictCursor,
            charset='utf8mb4'
        )
        return conn
    except OperationalError:
        return None

# 测试数据库是否连接成功
def test_database():
    conn = get_db_connection()
    if conn:
        conn.close()
        return True
    return False