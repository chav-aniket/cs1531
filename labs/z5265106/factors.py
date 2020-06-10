'''
NOTE: This exercise assumes you have completed divisors.py
'''

from divisors import divisors

# You may find this helpful
def is_prime(n):
    return n != 1 and divisors(n) == {1, n}

def factors(n):
    '''
    A generator that generates the prime factors of n. For example
    >>> list(factors(12))
    [2,2,3]

    Params:
      n (int): The operand

    Yields:
      (int): All the prime factors of n in ascending order.

    Raises:
      ValueError: When n is <= 1.
    '''
    keep_going = True
    prime_factors = divisors(n)
    while keep_going:
        keep_going = False
        for val in prime_factors:
            if divisors(val) > 2:
                keep_going = True
                prime_factors.append(divisors(val))
    return sorted(factors)
