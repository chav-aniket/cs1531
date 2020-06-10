'''
Tests for the core functionality of the helpr application
'''
import pytest
# Don't change this import line below. If your tests are black-box tests then
# you don't require any more functions from the module than these
from helpr import make_request, queue, remaining, help, resolve, cancel, revert, reprioritise, end

def test_sanity():
    '''
    A simple sanity test of the system.
    '''
    # DO NOT CHANGE THIS TEST! If you feel you have to change this test then
    # your functions have not been implemented correctly.
    student1 = "z1234567"
    description1 = "I don't understand how 'global' works in python"
    student2 = "z7654321"
    description2 = "What's the difference between iterator and iterable?"

    # Queue is initially empty
    assert queue() == []

    # Student 1 makes a request
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    assert remaining(student1) == 0

    # Student 2 makes a request
    make_request(student2, description2)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    assert remaining(student1) == 0
    assert remaining(student2) == 1

    # Student 1 gets help
    help(student1)
    assert queue() == [{"zid": student1, "description": description1, "status": "receiving"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    # Student 2 is now the only student "waiting" in the queue, so they have no
    # one remaining in front of them
    assert remaining(student2) == 0

    # Student 1 has their problem resolved
    resolve(student1)
    # Only student 2 is left in the queue
    assert queue() == [{"zid": student2, "description": description2, "status": "waiting"}]

    # Student is helped and their problem is resolved
    help(student2)
    resolve(student2)
    assert queue() ==[]

    # End the session
    end()

def zid(num=0):
    return 'z'+str(5555555+num)

@pytest.fixture()
def clear():
    end()

def test_make_request_empty_description(clear):
    '''
    Testing empty description in make_request()
    '''
    with pytest.raises(ValueError):
        make_request(zid(), "")

def test_make_request_double(clear):
    '''
    Testing one student making multiple requests in make_request()
    '''
    zid1 = zid()
    make_request(zid, "I am in need of assistance")
    with pytest.raises(KeyError):
        make_request(zid, "I am need halp plej")

def test_make_request_valid_input(clear):
    '''
    Testing valid input for make_request()
    '''
    assert make_request(zid(), "Yes me need help") is None

def test_queue_valid(clear):
    '''
    Testing correct return types for queue()
    '''
    make_request(zid(), "I need halp")
    queue_list = queue()
    assert isinstance(queue_list, list)
    for item in queue_list:
        assert isinstance(item, dict)

def test_remaining_no_request(clear):
    '''
    Testing for no request made in remaining()
    '''
    with pytest.raises(KeyError):
        remaining(zid())

def test_remaining_valid(clear):
    '''
    Testing valid input for remaining()
    '''
    zid1 = zid(1)
    zid2 = zid(2)
    zid3 = zid(3)
    make_request(zid1, "I need halp")
    ret = remaining(zid1)
    assert isinstance(ret, int) and ret == 0

    make_request(zid2, "No me first")
    ret = remaining(zid2)
    assert isinstance(ret, int) and ret == 1

    make_request(zid3, "No me first")
    ret = remaining(zid3)
    assert isinstance(ret, int) and ret == 2

def test_help_no_waiting_request(clear):
    '''
    Testing for if a student does not have a request
        with a 'waiting' status
    '''
    zid1 = zid(1)
    make_request(zid1, "I need halp")
    help(zid1)
    with pytest.raises(KeyError):
        help(zid1)

def test_help_valid(clear):
    '''
    Testing valid scenario of using help()
    '''
    zid1 = zid(1)
    make_request(zid1, "I need halp")
    assert help(zid1) is None

def test_resolve_no_receiving(clear):
    '''
    Testing if a student does not have a request with a 'receiving' status
    '''
    zid1 = zid(1)
    make_request(zid1, "I need halp")
    with pytest.raises(KeyError):
        resolve(zid1)

def test_resolve_valid(clear):
    '''
    Testing a valid scenario of using resolve()
    '''
    zid1 = zid(1)
    make_request(zid1, "I need halp")
    help(zid1)
    assert resolve(zid1) is None

def test_cancel_no_request_one(clear):
    '''
    Testing for no request in queue from student with 'waiting' status
    '''
    zid1 = zid(1)
    zid2 = zid(2)
    make_request(zid1, "I need halp")
    help(zid1)
    with pytest.raises(KeyError):
        cancel(zid1)
    with pytest.raises(KeyError):
        cancel(zid2)

def test_cancel_valid(clear):
    '''
    Testing a valid scenario of using cancel()
    '''
    zid1 = zid(1)
    make_request(zid1, "I need halp")
    cancel(zid1)

def test_revert_not_receiving(clear):
    '''
    Testing for if student does not have a receiving status request
    '''
    zid1 = zid(1)
    zid2 = zid(2)
    make_request(zid1, "I need halp")
    with pytest.raises(KeyError):
        revert(zid1)
    with pytest.raises(KeyError):
        revert(zid2)

def test_revert_valid(clear):
    '''
    Testing a valid scenario of using revert()
    '''
    zid1 = zid(1)
    make_request(zid1, "I need halp")
    help(zid1)
    assert revert(zid1) is None

def test_reprioritise_valid(clear):
    '''
    Testing if reprioritisation works
    '''
    zid1 = zid(1)
    zid2 = zid(2)
    zid3 = zid(3)
    zid4 = zid(4)
    make_request(zid1, "first request")
    make_request(zid2, "second request")
    make_request(zid3, "third request")
    help(zid1)
    resolve(zid1)
    help(zid2)
    resolve(zid2)
    make_request(zid1, "fourth request")
    make_request(zid2, "fifth request")
    help(zid2)
    resolve(zid2)
    make_request(zid2, "seventh request")
    make_request(zid4, "sixth request")
    assert queue() == [
        {"zid": zid3, "description": "third request", "status": "waiting"},
        {"zid": zid1, "description": "fourth request", "status": "waiting"},
        {"zid": zid2, "description": "seventh request", "status": "waiting"},
        {"zid": zid4, "description": "sixth request", "status": "waiting"}
    ]

    reprioritise()

    assert queue() == [
        {"zid": zid3, "description": "third request", "status": "waiting"},
        {"zid": zid4, "description": "sixth request", "status": "waiting"},
        {"zid": zid1, "description": "fourth request", "status": "waiting"},
        {"zid": zid2, "description": "seventh request", "status": "waiting"}
    ]

def test_end(clear):
    '''
    Testing usage of end()
    '''
    make_request(zid(), "I need halp")
    end()
    assert queue() == []
