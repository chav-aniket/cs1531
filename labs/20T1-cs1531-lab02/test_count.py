from count import count_char

def test_empty():
    assert count_char("") == {}

def test_simple():
    assert count_char("abc") == {"a": 1, "b": 1, "c": 1}

def test_double():
    assert count_char("aa") == {"a": 2}

def test_special():
    assert count_char("!@#$%^^") == {"!":1, "@":1, "#":1, "$":1, "%":1, "^":2}

def test_space():
    assert count_char("Hi there") == {"H":1, "i":1, " ":1, "t":1, "h":1, "e":2, "r":1}

def test_numbers():
    assert count_char("12342") == {"1":1, "2":2, "3":1, "4":1}