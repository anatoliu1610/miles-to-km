import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert b'healthy' in rv.data

def test_convert_valid(client):
    rv = client.post('/convert', json={'miles': 10})
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['miles'] == 10
    assert round(data['kilometers'], 4) == 16.0934

def test_convert_invalid(client):
    rv = client.post('/convert', json={'miles': 'abc'})
    assert rv.status_code == 400
    assert b'number' in rv.data

def test_convert_missing(client):
    rv = client.post('/convert', json={})
    assert rv.status_code == 400
    assert b'Missing' in rv.data

def test_convert_negative(client):
    rv = client.post('/convert', json={'miles': -5})
    assert rv.status_code == 400
    assert b'negative' in rv.data