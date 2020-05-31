from app import app
import pytest

# def test_sample():
#     assert 1 + 1 == 2

@pytest.fixture
def client():
    return app.test_client()

def do_get(client, path):
    response = client.get(path)
    return response.status_code, str(response.data), response.get_json()

def test_home(client):    
    # GET /
    # HTTP Status Code 200
    # Hello World
    status_code, body, data = do_get(client, '/')
    old_count = data['count']

    # response = client.get('/')
    assert status_code == 200
    assert '"text":"Hello. world"' in body


    # assert '"count":1' in str(response.data)
    '''
    curl localhost:5000  
    '''
    for i in range (5):
        status_code, body, data = do_get(client, '/')
        new_count = data['count']
        # response = client.get('/')
        assert status_code == 200
        assert '"text":"Hello. world"' in body

        
        # assert '"count":2' in str(response.data)
        assert new_count == old_count + i + 1

def test_abuse(client):           
    status_code, body, data = do_get(client, '/')
    old_count = data['count']
    assert status_code == 200
    assert '"text":"Hello. world"' in body    
    

    status_code, _, _ = do_get(client, '/abuse')
    assert status_code == 200
    
    status_code, body, data = do_get(client, '/')
    assert status_code == 200
    new_count = data['count']    
    assert new_count == old_count + 100 + 1
