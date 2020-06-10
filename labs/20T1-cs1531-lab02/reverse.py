def reverse_words(string_list):
    '''
    Given a list of strings, return a new list where the order of the words is$

    For example,
    >>> reverse_words(["Hello World", "I am here"])
    ['World Hello', 'here am I']
    '''
    ret = []
    for x in string_list:
        t = x.split(" ")
        t.reverse()
        r = " ".join(t)
        ret.append(r)
    return ret

def test_one():
    '''
    Tests the retention of capital letters
    '''
    list_one = ["Yes I am", "rAwR xDd", "my OH my"]
    list_one_reversed = ["am I Yes", "xDd rAwR", "my OH my"]
    assert reverse_words(list_one) == list_one_reversed

def test_two():
    '''
    Tests the retention of punctuation
    '''
    list_two = ["We're done here.", "mayhaps, we shall?", "no... I don't think I will"]
    list_two_reversed = ["here. done We're", "shall? we mayhaps,", "will I think don't I no..."]
    assert reverse_words(list_two) == list_two_reversed

def test_three():
    '''
    Tests the retention of double spaces
    '''
    list_three = ["spaces  here", "  leading trailing  "]
    list_three_reversed = ["here  spaces", "  trailing leading  "]
    assert reverse_words(list_three) == list_three_reversed

def test_four():
    '''
    Tests empty strings
    '''
    list_four = ["", ""]
    list_four_reversed = ["", ""]
    assert reverse_words(list_four) == list_four_reversed

def test_five():
    '''
    Tests what happens when there are no spaces
    '''
    list_five = ["aiwuy./er,g/?ar!?><aR?v.,arb"]
    list_five_reversed = ["aiwuy./er,g/?ar!?><aR?v.,arb"]
    assert reverse_words(list_five) == list_five_reversed
