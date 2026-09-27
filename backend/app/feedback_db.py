import sqlite3
from typing import Dict, Any
from .config import settings

def init_db():
    conn = sqlite3.connect(settings.SQLITE_DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            simplified_text TEXT,
            feedback_type TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_feedback(text: str, simplified_text: str, feedback_type: str):
    conn = sqlite3.connect(settings.SQLITE_DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO feedback (text, simplified_text, feedback_type) VALUES (?, ?, ?)",
        (text, simplified_text, feedback_type)
    )
    conn.commit()
    conn.close()
