'''
Lab05 Exercise 7
'''
import datetime

class Student:
    '''
    Creates a student object with name, birth year
    and class age method
    '''
    def __init__(self, firstName, lastName, birth_year):
        self.name = firstName + " " + lastName
        self.birth_year = birth_year

    def age(self):
        '''
        Added this function to encapsulate the age
        '''
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def print_age(self):
        '''
        Used to print out the age
        '''
        print(f"{self.name} is {self.age()} years old")

if __name__ == '__main__':
    NEW = Student("Rob", "Everest", 1961)
    NEW.print_age()
