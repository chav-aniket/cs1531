'''
I HATE PYLINT
Lab05 Exercise 3
'''
from urllib import request
import json

def add(payload):
    '''
    Function for /name/add route to add names to the server
    '''
    url = 'http://127.0.0.1:7117/name/add'
    headers = {'Content-Type':'application/json'}
    data = json.dumps(payload).encode('utf-8')
    req = request.Request(url=url, data=data, headers=headers, method='POST')
    return json.loads(request.urlopen(req).read())

def get():
    '''
    Function for /names route to display names from the server
    '''
    url = 'http://127.0.0.1:7117/names'
    # headers = {'Content-Type':'application/json'}
    req = request.Request(url=url)
    return json.loads(request.urlopen(req).read())

def delete(payload):
    '''
    Function for /name/remove route to delete a certain name from the server
    '''
    url = 'http://127.0.0.1:7117/name/remove'
    headers = {'Content-Type':'application/json'}
    data = json.dumps(payload).encode('utf-8')
    req = request.Request(url=url, data=data, headers=headers, method='DELETE')
    return json.loads(request.urlopen(req).read())

def reset():
    '''
    Function for /name/reset to clear all the names from the server
    '''
    url = 'http://127.0.0.1:7117/name/reset'
    headers = {'Content-Type':'application/json'}
    req = request.Request(url=url, headers=headers, method='DELETE')
    return json.loads(request.urlopen(req).read())

def test_one():
    '''
    Tests connecting to the server and name/add route
    '''
    assert reset() == {}
    assert add({"name":"Hayden"}) == {}
    assert get()['name'] == "['Hayden']"

def test_two():
    '''
    Tests adding multiple names
    '''
    assert reset() == {}
    assert add({"name":"Hayden"}) == {}
    assert add({"name":"Karim"}) == {}
    assert add({"name":"Tina"}) == {}
    assert add({"name":"Ashish"}) == {}
    assert get()['name'] == "['Hayden', 'Karim', 'Tina', 'Ashish']"

def test_three():
    '''
    Tests deleting a single name at the front
    '''
    assert reset() == {}
    assert add({"name":"Hayden"}) == {}
    assert add({"name":"Karim"}) == {}
    assert add({"name":"Tina"}) == {}
    assert add({"name":"Ashish"}) == {}
    assert get()['name'] == "['Hayden', 'Karim', 'Tina', 'Ashish']"
    assert delete({"name":"Hayden"}) == {}
    assert get()['name'] == "['Karim', 'Tina', 'Ashish']"

def test_four():
    '''
    Tests deleting multiple names from any position
    '''
    assert reset() == {}
    assert add({"name":"Hayden"}) == {}
    assert add({"name":"Karim"}) == {}
    assert add({"name":"Tina"}) == {}
    assert add({"name":"Ashish"}) == {}
    assert get()['name'] == "['Hayden', 'Karim', 'Tina', 'Ashish']"
    assert delete({"name":"Karim"}) == {}
    assert delete({"name":"Ashish"}) == {}
    assert get()['name'] == "['Hayden', 'Tina']"

# def test_five():
#     '''
#     Tests deleting a name that doesn't exist on the server
#     '''
#     assert reset() == {}
#     assert add() == {}
#     assert delete({"name":"Karim"})['error'] == "Name does not exist"
