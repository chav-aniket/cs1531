from reduce import reduce

def test_one():
    '''
    Testing for non-lists
    '''
    reduce(lambda x, y: x + y, 'iufydt') == 'iufydt'

def test_two():
    '''
    Testing with empty list
    '''
    reduce(lambda x, y: x + y, []) == None

def test_three():
    '''
    Testing with valid input and addition function
    '''
    print(reduce(lambda x, y: x + y, [1,2,3,4,5])) == 15

def test_four():
    '''
    Testing with valid input and multiplication function
    '''
    print(reduce(lambda x, y: x * y, [1,2,3,4,5])) == 120

def test_five():
    '''
    Testing with single value in list
    '''
    print(reduce(lambda x, y: x + y, [360]))