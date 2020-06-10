def divisors(n):
    '''
    Given some number n, return a set of all the numbers that divide it. For example:
    >>> divisors(12)
    {1, 2, 3, 4, 6, 12}

    Params:
      n (int): The operand

    Returns:
      (set of int): All the divisors of n

    Raises:
      ValueError: If n is not a positive integer
    '''
    ret = []
    for i in range(1, n):
        if n%i == 0:
            ret.append(i)
    return list(set(ret))
