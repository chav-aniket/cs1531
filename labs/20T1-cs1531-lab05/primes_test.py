'''
Test file for factors function
'''
from primes import factors

def test_one():
    '''
    testing for 1
    '''
    assert factors(1) == [1]

def test_two():
    '''
    testing for 2^10
    '''
    assert factors(1024) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

def test_three():
    '''
    testing for the product of a series of primes
    '''
    assert factors(15015) == [3, 5, 7, 11, 13]
