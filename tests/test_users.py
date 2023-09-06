from fastapi.testclient import TestClient
from main import app
from models.users import UserCreate

client = TestClient(app)


def test_create_user():
    user_data = {"username": "testuser", "password": "testpassword"}
    response = client.post("/api/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
