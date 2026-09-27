from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.retrieval.retriever import search
from tax_guide_corpus.build_index import build_index
import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_index():
    build_index()

def test_search_function():
    chunks, sources = search("What is Form 16?")
    assert len(chunks) > 0
    assert len(sources) > 0

def test_guide_endpoint():
    with TestClient(app) as client:
        response = client.post(
            "/guide/query",
            json={"query": "How to file ITR late?", "lang": "en"}
        )
        assert response.status_code == 200
        data = response.json()
        assert "answer_chunks" in data
        assert "sources" in data
        assert len(data["answer_chunks"]) > 0
