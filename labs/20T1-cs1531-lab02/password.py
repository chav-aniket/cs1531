def check_password(password):
    '''
    Takes in a password, and returns a string based on the strength of that password.

    The returned value should be:
    * "Strong password", if at least 12 characters, contains at least one number, at least one uppercase letter, at least one lowercase letter.
    * "Moderate password", if at least 8 characters, contains at least one number.
    * "Poor password", for anything else
    * "Horrible password", if the user enters "password", "iloveyou", or "123456"
    '''
    if password=="password" or password=="iloveyou" or password=="123456":
        return "Horrible password"
    elif len(password)>=12:
        if (any(x.isupper() for x in password) and 
            any(x.islower() for x in password) and
            any(x.isdigit() for x in password)):
            return "Strong password"
        elif any(x.isdigit() for x in password):
            return "Moderate password"
        else:
            return "Poor password"
    elif len(password)>=8:
        if any(x.isdigit() for x in password):
            return "Moderate password"
        else:
            return "Poor password"
    else:
        return "Poor password"

if __name__ == '__main__':
    print(check_password("ihearttrimesters"))
    print(check_password("123456"))
    print(check_password("iH3artTrimesters"))
    print(check_password("iheart"))
    print(check_password("ih3arttrimesters"))
    print(check_password("iHeart"))
    # What does this do?
    '''
    It's an import guard, entering the body of the if statement only in this file itself
    and not if this file is being imported elsewhere
    '''
def test_one():
    assert check_password("123456") == "Horrible password"

def test_two():
    assert check_password("iH3artTrimesters") == "Strong password"

def test_three():
    assert check_password("iheart") == "Poor password"

def test_four():
    assert check_password("ih3arttrimesters") == "Moderate password"

def test_five():
    assert check_password("iHeart") == "Poor password"