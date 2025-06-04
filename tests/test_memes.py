from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_upload_and_get_meme():
    meme = {
        "title": "Grumpy",
        "url": "/catmemes/grumpy.png",
        "uploaded_by": "catlover"
    }
    response = client.post("/api/memes", json=meme)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Grumpy"

    get_response = client.get(f"/api/memes/{data['id']}")
    assert get_response.status_code == 200
