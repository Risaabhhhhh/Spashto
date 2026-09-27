from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.models.simplifier import simplify_text

def test_simplify_model():
    # Directly test the function
    result = simplify_text("The assessee shall be liable to penalty.", "en")
    assert isinstance(result, str)
    assert len(result) > 0

def test_simplify_endpoint():
    with TestClient(app) as client:
        response = client.post(
            "/simplify",
            json={"text": "The assessee shall be liable to penalty.", "target_lang": "en"}
        )
        assert response.status_code == 200
        assert "simplified_text" in response.json()
