import json
import sys
import os
import chromadb
from sentence_transformers import SentenceTransformer

# Add parent to path for config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.app.config import settings

def build_index():
    print("Building tax guide index...")
    client = chromadb.PersistentClient(path=settings.CHROMA_DB_DIR)
    
    # Delete collection if exists to rebuild
    try:
        client.delete_collection("tax_guide")
    except Exception:
        pass
        
    collection = client.create_collection("tax_guide")
    embedder = SentenceTransformer(settings.EMBEDDING_MODEL_NAME)
    
    with open("tax_guide_corpus/scenarios.jsonl", "r") as f:
        docs = [json.loads(line) for line in f]
        
    documents = []
    metadatas = []
    ids = []
    embeddings = []
    
    for i, doc in enumerate(docs):
        text = f"{doc['condition']}. {doc['guidance_text']}"
        documents.append(doc['guidance_text'])
        metadatas.append({
            "source_url": doc['source_url'],
            "assessment_year": doc['assessment_year'],
            "condition": doc['condition']
        })
        ids.append(f"doc_{i}")
        # e5-small requires 'passage: ' prefix for documents
        emb = embedder.encode(f"passage: {text}").tolist()
        embeddings.append(emb)
        
    collection.add(
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )
    
    print(f"Successfully indexed {len(docs)} scenarios into ChromaDB.")

if __name__ == "__main__":
    build_index()
