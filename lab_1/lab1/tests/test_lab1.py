from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_main():
    response = client.get("/") # get the root endpoint
    assert response.status_code == 501 # check response status is 501
    assert response.json() == {'detail': 'Not Implemented'} # check response

def test_hello():
    for name in ['Luis',1, '10','None']:
        response = client.get("/hello", params={"name": name})
        assert response.status_code == 200
        assert response.json() == {"message": f"Hello {name}"}

def test_hello_bad():
    response = client.get("/hello")
    assert response.status_code == 400
    assert response.json() == {'detail': 'Name must be specified, please type /hello?name={name}'}

def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200

def test_openapi_json():
    response = client.get("/openapi.json")
    assert response.status_code == 200
