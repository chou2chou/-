import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    PROJECT_NAME = "deaf-edu-agent"
    REDIS_URL = "redis://localhost:6379/0"
    
    # MySQL 配置（这里不用改，后面我教你）
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PWD = "123456"
    MYSQL_DB = "deaf_agent"
    
    CHROMA_DB_DIR = "./chroma_db"

settings = Settings()