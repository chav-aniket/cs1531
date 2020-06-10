from list_exercises import *

def test_reverse():
    l = ["how", "are", "you"]
    m = []
    n = ["with 4 words", "it works", "see how", "let's"]

    reverse_list(l)
    reverse_list(m)
    reverse_list(n)
    
    assert l == ["you", "are", "how"]
    assert m == []
    assert n == ["let's", "see how", "it works", "with 4 words"]

def test_min():
    assert minimum([1, 2, 3, -10]) == -10
    assert minimum([1, 1, 1]) == 1
    assert minimum(['a', 'b', 'c']) == 'a'

def test_sum():
    assert sum_list([7, 7, 7]) == 21
    assert sum_list([]) == 0
    assert sum_list([7, -7, 7]) == 7
