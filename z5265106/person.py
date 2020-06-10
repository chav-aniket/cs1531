'''
Person Exercise
'''

class Person:
    '''
    A named person.
    '''
    def __init__(self, name_first, name_last=None):
        self._firstname = name_first
        self._lastname = name_last

    @property
    def first_name(self):
        return self._firstname

    @property
    def last_name(self):
        return self._lastname

    @property
    def full_name(self):
        if self.last_name is None:
            return self.first_name
        return self.first_name + ' ' + self.last_name

    @first_name.setter
    def first_name(self, name_first):
        self._firstname = name_first

    @last_name.setter
    def last_name(self, name_last):
        self._lastname = name_last

    @full_name.setter
    def full_name(self, name_full):
        self._firstname = name_full.split()[0].strip()
        self._lastname = name_full.split()[-1].strip()


# Do NOT change any code below this line

def test_simple():
    '''
    Check that Person tracks first, last and full name
    '''
    john = Person("John", "Smith")
    assert john.first_name == "John"
    assert john.last_name == "Smith"
    assert john.full_name == "John Smith"

def test_name_change():
    '''
    Check that names can be changed
    '''
    teacher = Person("Hayden", "Smith")
    teacher.first_name = "Rob"
    assert teacher.first_name == "Rob"
    assert teacher.full_name == "Rob Smith"

    teacher.last_name = "Everest"
    assert teacher.last_name == "Everest"
    assert teacher.full_name == "Rob Everest"

    teacher.full_name = "Simon Haddad"
    assert teacher.first_name == "Simon"
    assert teacher.last_name == "Haddad"

def test_single_name():
    '''
    Some people only have one name.
    '''
    madonna = Person("Madonna", None)
    assert madonna.first_name == "Madonna"
    assert madonna.last_name is None
    assert madonna.full_name == "Madonna"

def test_spaces():
    '''
    Extra spaces should be ignored.
    '''
    tutor = Person("Michelle", "Seeto")
    tutor.full_name = "Vivian  Dang" # Note one extra space

    # No spaces in name components
    assert tutor.first_name == "Vivian"
    assert tutor.last_name == "Dang"