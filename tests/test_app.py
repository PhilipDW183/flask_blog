from blog_app import app

def test_app_running():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200

def test_app_visible():
    with app.test_client() as client:
        response = client.get("/")
        assert b'Hello, World' in response.data