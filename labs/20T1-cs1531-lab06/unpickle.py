'''
Labo06 Exercise 1
'''
import json
import operator
from pickle import load
from process import pack

DATA = load(open("shapecolour.p", "rb"))
FREQ = {}

def keygen(dictionary):
    '''
    Concatenates dictionary values to make a key
    '''
    shape = dictionary['shape']
    colour = dictionary['colour']
    return shape + '-' + colour

for x in DATA:
    key = keygen(x)
    if key not in FREQ:
        FREQ[key] = 0
    FREQ[key] += 1

KEY = max(FREQ.items(), key=operator.itemgetter(1))[0]
SHAPE, COLOUR = KEY.split('-')
print(f"Colour: {COLOUR}")
print(f"Shape: {SHAPE}")

pack(COLOUR, SHAPE, DATA)
