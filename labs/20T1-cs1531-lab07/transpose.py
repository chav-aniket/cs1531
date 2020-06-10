from functools import reduce

def transpose(matrix):
    '''
    Given a matrix, calculate its transpose. Transposing a matrix swaps its rows
    with its columns, so the element at position (i,j) of the matrix is now at
    position (j,i).

    Params:
        matrix (list): A matrix represented as a list of lists, where each inner
        list is of the same length.

    Returns:
        (list): The transposed matrix, represented as a lists of lists where
        each inner list is the same length.

    Raises:
        ValueError: If the inner lists of the argument are not all of the same
        length.
    '''
    if matrix == [[]]:
        return matrix
    else:
        if all(map(lambda x: len(x) == len(matrix[0]), matrix)):
            return list(map(lambda *a: list(a), *matrix))
        else:
            raise ValueError

def test_0x0():
    assert transpose([[]]) == [[]]

def test_1x1():
    assert transpose([[1]]) == [[1]]

def test_2x1():
    assert transpose([[1,2]]) == [[1],[2]]

def test_2x2():
    assert transpose([[1,2], [3,4]]) == [[1,3], [2,4]]

def test_2x3():
    assert transpose([[1,2], [3,4], [5,6]]) == [[1,3,5], [2,4,6]]

def test_3x3():
    assert transpose([[1,2,3], [4,5,6], [7,8,9]]) == [[1,4,7], [2,5,8], [3,6,9]]
