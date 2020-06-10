import statistics
from functools import reduce
import pytest

def rainfall(nums):
    positive = list(filter(lambda x: x >= 0, nums))
    if positive is None:
        raise ValueError
    return statistics.math.ceil(statistics.mean(positive))

def test_simple():
    assert rainfall([1, 2, 3]) == 2

def test_negative():
    assert rainfall([1, -5, 3, 4, 4]) == 3

def test_zero():
    assert rainfall([1, 0, 2, 3]) == 2

def test_empty():
    with pytest.raises(ValueError):
        rainfall([-1, -2, -3])
