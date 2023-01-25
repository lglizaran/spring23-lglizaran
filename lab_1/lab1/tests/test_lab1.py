from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_main():
    response = client.get("/") # get the root endpoint
    assert response.status_code == 501 # check response status is 501
    assert response.json() == {'detail': 'Not Implemented'} # check response

def test_hello():
    response = client.get("/hello/", params={"name": "foo"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello foo"}

def test_hello_bad():
    response = client.get("/hello/")
    assert response.status_code == 400
    assert response.json() == {'detail': 'Name must be specified, please type /home/?name={name}'}

def test_docs():
    response = client.get("/docs/")
    assert response.status_code == 200
    # assert response.json() == {"message": "Hello foo"}

def test_openapi_json():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    # assert response.json() == {"message": "Hello foo"}