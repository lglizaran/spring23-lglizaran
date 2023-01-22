from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_main():
    response = client.get("/") # get the root endpoint
    assert response.status_code == 200 # check response status is 200
    assert response.json() == {"message": "Hello World"} # check response