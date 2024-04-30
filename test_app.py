import pytest
from flask import url_for
from app import app  

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_display_login(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_login(client):
    rv = client.post('/', data={'username': 'test', 'password': 'test'})
    assert rv.status_code == 200

def test_display_register(client):
    rv = client.get('/register')
    assert rv.status_code == 200

def test_register(client):
    rv = client.post('/register', data={'name': 'test', 'username': 'test', 'password': 'test'})
    assert rv.status_code == 200

def test_display_home(client):
    rv = client.get('/home/test')
    assert rv.status_code == 200

def test_display_query(client):
    rv = client.get('/query/sport/test')
    assert rv.status_code == 200

def test_display_profile(client):
    rv = client.get('/profile/test')
    assert rv.status_code == 200

def test_profile(client):
    rv = client.post('/profile/test', data={'username': 'test'})
    assert rv.status_code == 200

def test_query(client):
    rv = client.post('/query/sport', data={'sport': 'test'})
    assert rv.status_code == 200
