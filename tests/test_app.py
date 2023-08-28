import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert b'Welcome to the Nationalize App' in response.data

def test_get_nationality(client):
    response = client.post('/', data={'name': 'test'})
    assert b'Name: test' in response.data
