import sys

def roman(input):
    roman = input.upper()
    convert = {'I':[1,0], 'V':[5,1], 'X':[10,0], 'L':[50,1], 'C':[100,0], 'D':[500,1], 'M':[1000,0]}
    decimal = 0

    skip = False
    for i in range(0, len(roman)):
        print(f"Evaluating {roman[i]}")
        if skip:
            skip = False
            continue
        
        def val(i, index):
            return convert.get(roman[i])[index]

        if i < len(roman) - 1:
            if roman[i] not in convert or roman[i+1] not in convert:
                print("Invalid Roman Numeral")
                exit()
            if val(i,0) < val(i+1,0) and not val(i,1):
                decimal += (val(i+1,0)-val(i,0))
                print(f"Case 1: Added {val(i+1,0)-val(i,0)}")
                skip = True
                continue
        decimal += val(i,0)
        print(f"Case 2: Added {val(i,0)}")
    return decimal

def test_one():
    '''
    Testing all possible values are recognised
    '''
    assert roman('MDCLXVI') == 1666, 'MDCLXVI == 1666'

def test_two():
    '''
    Testing all subtractive situations
    '''
    assert roman('IV') == 4, 'IV == 4'
    assert roman('IX') == 9, 'XIX == 19'
    assert roman('XL') == 40, 'XL == 40'
    assert roman('XC') == 90, 'XC == 90'
    assert roman('CD') == 400, 'CD == 400'
    assert roman('CM') == 900, 'CM == 900'

def test_three():
    '''
    Testing combinations of subtractive forms within numbers
    and other such complicated examples
    '''
    assert roman('XIX') == 19, 'XIX == 19'
    assert roman('MMMDCCCLXXXVIII') == 3888, 'MMMDCCCLXXXVIII == 3888'
    assert roman('MCDXLIV') == 1444, 'MCDXLIV == 1444'
    assert roman('MCMXCIX') == 1999, 'MCMXCIX == 1999'
