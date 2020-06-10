'''
Lab06 Exercise 7
'''
import math
class Circle:
    '''
    This class is a circle :)
    '''
    def __init__(self, radius):
        self.radius = float(radius)
    def calc_circumference(self, print_bool):
        '''
        Calculates and returns the circumference
        '''
        circumference = round(self.radius * 2 * math.pi, 1)
        if print_bool is True:
            print(f"Circumference: {circumference}")
        return circumference
    def calc_area(self, print_bool):
        '''
        Calculates and returns the area
        '''
        area = round(math.pi * self.radius**2)
        if print_bool is True:
            print(f"Area: {area}")
        return area

NEW = Circle(input("Please enter a radius: "))
NEW.calc_circumference(True)
NEW.calc_area(True)
