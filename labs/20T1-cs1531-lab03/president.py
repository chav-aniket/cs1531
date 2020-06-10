president = {
    'name' : 'Ian Jacobs',
    'age' : 54,
    'staff' : [ 'Sally', 'Bob', 'Rob', 'Hayden' ]
}

## TODO: Write code below this line

if __name__ == '__main__':
    president.get('staff').remove('Hayden')
    president.get('staff').sort()
    president['marks'] = {"20T1":77, "20T2":88, "20T2":99}

## TODO: Write code above this line
