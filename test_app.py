import pytest
from app import app
from stats_api import search_statmuse  

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_display_login(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_login(client):
    rv = client.get('/', data={'username': 'test', 'password': 'test'})
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

def test_display_profile(client):
    rv = client.get('/profile/test')
    assert rv.status_code == 200

def test_display_addfriends(client):
    rv = client.get('/addfriends/test')
    assert rv.status_code == 200

def test_addfriends(client):
    rv = client.post('/addfriends/test', data={'friend': 'test'})
    assert rv.status_code == 200

def test_display_query(client):
    rv = client.post('/query/test/', data={'sport': 'nba', 'query': 'brunson'})
    assert rv.status_code == 200

def test_search_statmuse():
    # Test with a known query and sport
    result = search_statmuse('who is the highest scoring player in the NBA', 'nba')
    assert 'Sorry, I dont\'t understand your question.' not in result

    # Test with an unknown sport
    result = search_statmuse('who is the highest scoring player in the NBA', 'unknown_sport')
    assert 'Sorry, I dont\'t understand your question.' in result

    # Test with an unknown query
    result = search_statmuse('unknown query', 'nba')
    assert 'Sorry, I dont\'t understand your question.' in result