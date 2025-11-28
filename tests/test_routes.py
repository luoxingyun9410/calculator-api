import pytest
from api import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_add(client):
    response = client.get('/add/3/5')
    assert response.status_code == 200
    assert response.get_json() == {"result": 8}

def test_subtract(client):
    response = client.get('/subtract/10/4')
    assert response.status_code == 200
    assert response.get_json() == {"result": 6}

def test_multiply(client):
    response = client.get('/multiply/6/7')
    assert response.status_code == 200
    assert response.get_json() == {"result": 42}

def test_divide(client):
    response = client.get('/divide/20/4')
    assert response.status_code == 200
    assert response.get_json() == {"result": 5.0}

def test_divide_by_zero(client):
    response = client.get('/divide/10/0')
    assert response.status_code == 400
    assert response.get_json() == {"error": "Cannot divide by zero"}