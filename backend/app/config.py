import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_NAME: str = "google/mt5-small"
    EMBEDDING_MODEL_NAME: str = "intfloat/multilingual-e5-small"
    CHROMA_DB_DIR: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "chroma_db")
    SQLITE_DB_PATH: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "feedback.db")
    
settings = Settings()
