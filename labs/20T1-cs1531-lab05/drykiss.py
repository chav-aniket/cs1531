'''
I HATE PYLINT
Lab05 Exercise 4
'''
from functools import reduce
from operator import mul

if __name__ == '__main__':
    # Made an empty list to store inputs in
    MY_LIST = []
    # Iterated through a string "abcde" to reduce repetition of input lines
    for c in "abcde":
        MY_LIST.append(int(input(f"Enter {c}: ")))
    print(f"Minimum: {min(MY_LIST)}")
    # Used reduce with mul operator to multiply 
    #   the FIRST 4 elements of the string using splicing
    print(f"Product of first 4 numbers: \n  {reduce(mul, MY_LIST[0:4])}")
    # Used reduce with mul operator to multiply 
    #   the LAST 4 elements of the string using splicing
    print(f"Product of last 4 numbers \n  {reduce(mul, MY_LIST[-4:])}")

    #---------------------------------------------------------------------------------

    # OLD CODE

    # a = input("Enter a: ")
    # a = int(a)
    # b = input("Enter b: ")
    # b = int(b)
    # c = input("Enter c: ")
    # c = int(c)
    # d = input("Enter d: ")
    # d = int(d)
    # e = input("Enter e: ")
    # e = int(e)
    # my_list = [a, b, c, d, e]
    # my_min = 999999
    # for i in range(0, 5):
    #     if my_list[i] < my_min:
    #         my_min = my_list[i]
    # print("Minimum: " + str(my_min))
    # print("Product of first 4 numbers: ")
    # product = 1
    # for i in range(0, 4):
    #     product = product * my_list[i]
    # print(f"  {product}")

    # print("Product of last 4 numbers")
    # product = 1
    # for i in range(1, 5):
    #     product = product * my_list[i]
    # print(f"  {product}")
