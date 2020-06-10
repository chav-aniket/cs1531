'''
I HATE PYLINT
Lab05 Exercise 5
'''
def factors(num):
    '''
    Takes num and returns its prime factorisation
    '''
    if num < 1:
        print("Choose a number above 0 please")
        exit()
    elif num == 1:
        print(1)
        return [1]
    factors_list = []
    curr = num
    for i in range(2, curr):
        while curr % i == 0:
            factors_list.append(i)
            curr = int(curr/i)
        if curr == 1:
            break
    print(" ".join(str(i)) for i in factors_list)
    return factors_list
