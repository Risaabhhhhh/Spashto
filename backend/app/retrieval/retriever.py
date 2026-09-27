import chromadb
from ..config import settings
from ..models.embedder import get_embedding

_client = None
_collection = None

def get_collection():
    global _client, _collection
    if _client is None:
        _client = chromadb.PersistentClient(path=settings.CHROMA_DB_DIR)
        _collection = _client.get_or_create_collection("tax_guide")
    return _collection

def search(query: str, n_results: int = 3):
    collection = get_collection()
    query_embedding = get_embedding(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    
    answer_chunks = []
    sources = []
    
    if results['documents'] and len(results['documents']) > 0:
        for i in range(len(results['documents'][0])):
            doc = results['documents'][0][i]
            meta = results['metadatas'][0][i] if results['metadatas'] else {}
            answer_chunks.append(doc)
            if 'source_url' in meta:
                sources.append(meta['source_url'])
                
    return answer_chunks, list(set(sources))
