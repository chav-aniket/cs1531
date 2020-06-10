'''
HTTP tests for the helpr application
'''

import config
import pytest
from requests import get, delete, post

# Do NOT change this URL! If you need to change the port number, change the
# value in config.py
BASE_URL=f"http://127.0.0.1:{config.PORT}"

def make_request(payload):
    '''
    Handler for making new request
    '''
    global BASE_URL
    url = BASE_URL+'/make_request'
    req = post(url=url, json=payload)
    return req.json()

def queue():
    '''
    Handler for fetching the queue
    '''
    global BASE_URL
    url = BASE_URL+'/queue'
    req = get(url=url)
    return req.json()

def remaining(payload):
    '''
    Handler for asking how many people ahead
    '''
    global BASE_URL
    url = BASE_URL+'/remaining/'+payload
    req = get(url=url)
    return req.json()

def help(payload):
    '''
    Handler for setting a request status to 'receiving'
    '''
    global BASE_URL
    url = BASE_URL+'/help'
    req = get(url=url, json=payload)
    return req.json()

def resolve(payload):
    '''
    Handler for resolving a request
    '''
    global BASE_URL
    url = BASE_URL+'/resolve'
    req = get(url=url, json=payload)
    return req.json()

def cancel(payload):
    '''
    Handler for cancelling a request
    '''
    global BASE_URL
    url = BASE_URL+'/cancel'
    req = get(url=url, json=payload)
    return req.json()

def revert(payload):
    '''
    Handler for reverting a request back to 'waiting' status
    '''
    global BASE_URL
    url = BASE_URL+'/revert'
    req = get(url=url, json=payload)
    return req.json()

def reprioritise():
    '''
    Handler for reprioritising queue
    '''
    global BASE_URL
    url = BASE_URL+'/reprioritise'
    req = get(url=url)
    return req.json()

def end():
    '''
    Handler for ending session
    '''
    global BASE_URL
    url = BASE_URL+'/end'
    req = get(url=url)
    return req.json()

def test_make_request_route():
    '''
    test for make_request()
    '''
    pkt = {
        'zid': '5555555',
        'description': 'Hello'
    }
    ret = make_request(pkt)
    assert ret = {}

def test_queue_route():
    '''
    test for queue()
    '''
    pkt = {
        'zid': '5555555',
        'description': 'Hello'
    }
    ret = make_request(pkt)
    ret = queue()
    assert ret = {}

def test_remaining_route():
    '''
    test for remaining()
    '''
    pkt = {
        'zid': '5555555',
        'description': 'Hello'
    }
    ret = make_request(pkt)
    pkt1 = {
        'zid': '5555555',
        'description': 'Bye'
    }
    ret = make_request(pkt1)
    ret = remaining('5555556')
    assert ret = {}

def test_help_route():
    '''
    test for help()
    '''
    pkt = {
        'zid': '5555555',
        'description': 'Hello'
    }
    ret = make_request(pkt)
    pkt1 = {
        'zid': '5555555'
    }
    ret = help(pkt1)
    assert ret = {}

def test_cancel_route():
    '''
    test for cancel()
    '''
    pkt = {
        'zid': '5555555',
        'description': 'Hello'
    }
    ret = make_request(pkt)
    pkt1 = {
        'zid': '5555555'
    }
    ret = cancel(pkt1)
    assert ret = {}

def test_revert_route():
    '''
    test for revert()
    '''
    pkt = {
        'zid': '5555555',
        'description': 'Hello'
    }
    ret = make_request(pkt)
    pkt1 = {
        'zid': '5555555'
    }
    ret = revert(pkt1)
    assert ret = {}

def test_reprioritise_route():
    '''
    test for reprioritise()
    '''
    ret = reprioritise()
    assert ret = {}

def test_end_route():
    '''
    test for end()
    '''
    ret = end()
    assert ret = {}