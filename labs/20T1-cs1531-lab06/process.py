'''
Lab06 Exercise 2
'''
import json
from pickle import load

def pack(colour, shape, data):
    '''
    packs given parameters into specified json structure
    '''
    ret = {
        'mostCommon': {
            'colour': colour, 
            'shape': shape
        }, 
        'rawData': load(open("shapecolour.p", "rb"))
    }

    with open('processed.json', 'w', encoding='utf-8') as FILE:
        json.dump(ret, FILE, ensure_ascii=False, indent=4)
    return ret
