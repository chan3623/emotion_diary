import os
import mysql.connector
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE"),
        port=int(os.getenv("DB_PORT"))
    )

def init_db():
    """테이블이 없을 경우 초기 생성합니다."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS diaries (
        id INT AUTO_INCREMENT PRIMARY KEY,
        diary_date DATE NOT NULL,
        emotion_score INT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()