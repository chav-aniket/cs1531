from prefix import prefix_search
import pytest

def test_documentation():
    assert prefix_search({"ac": 1, "ba": 2, "ab": 3}, "a") == { "ac": 1, "ab": 3}

def test_exact_match():
    assert prefix_search({"category": "math", "cat": "animal"}, "cat") == {"category": "math", "cat": "animal"}

def test_empty():
    assert prefix_search({}, 'a') == {}

def test_no_prefix_found():
    assert prefix_search({'hello':'world', 'hi':'there'}, 'no') == {}

def test_only_prefix():
    assert prefix_search({'no':'way', 'no':'ok', 'ono':'ouo'}, 'no') == {'no':'way', 'no':'ok'}

def test_spaces():
    assert prefix_search({'no way': 'jose', 'n o':'ok...', ' nooooo':"ok I'll stop..."}, 'no') == {'no way': 'jose'}

def test_empty_prefix():
    assert prefix_search({'blarg':'no you', 'blargblarg':'stfu'}, '') == {'blarg':'no you', 'blargblarg':'stfu'}