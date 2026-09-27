from sentence_transformers import SentenceTransformer
from ..config import settings

_embedder = None

def load_embedder():
    global _embedder
    if _embedder is None:
        print(f"Loading embedder model: {settings.EMBEDDING_MODEL_NAME}")
        _embedder = SentenceTransformer(settings.EMBEDDING_MODEL_NAME)

def get_embedding(text: str):
    if _embedder is None:
        load_embedder()
    # e5 requires prefix "query: " or "passage: " usually
    return _embedder.encode(f"query: {text}").tolist()
