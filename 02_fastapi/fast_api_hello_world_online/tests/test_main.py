from fastapi.testclient import TestClient
from fast_api_hello_world_online.main import app


def test_root_path():
    client = TestClient(app=app)# left app is parameter and right one is variable
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello":"World"}

def test_piaic_des():
    client = TestClient(app=app)
    response = client.get('/piaic')
    assert response.status_code == 200
    assert response.json() == {"Organization": "piaic"}