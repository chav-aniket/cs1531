'''
Lab06 Exercise 5
'''
def reduce(func, array):
    '''
    A function to reduce a list based on a given function
    '''
    if not isinstance(array, list):
        return array
    if not array:
        return None
    if len(array) == 1:
        return array[0]
    prev = func(array[0], array[1])
    for i in range(2, len(array)):
        prev = func(prev, array[i])
    return prev

if __name__ == '__main__':
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
    print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))
