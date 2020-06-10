'''
Lab06 Exercise 4
'''
import sys
import csv
import datetime
from math import fabs

if len(sys.argv) != 3:
    print("Invalid Input")
    exit()
elif not isinstance(sys.argv[1], str) or not isinstance(sys.argv[2], str):
    print("Invalid Input")
    exit()

DATE = sys.argv[1]
LOCATION = sys.argv[2]

DAY, MONTH, YEAR = DATE.split('-')
DATE = YEAR+'-'+MONTH+'-'+DAY
try:
    datetime.datetime(int(YEAR), int(MONTH), int(DAY))
except ValueError:
    print("Invalid input")

WEATHER = {}
MIN_TEMP = 0
MAX_TEMP = 0
AVG_MIN = 0
AVG_MAX = 0
LOCATION_FOUND = False
with open('weatherAUS.csv', newline='') as csvfile:
    CUR = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(CUR)
    for row in CUR:
        # print(row)
        record = row[0].split(",")
        # print(record)
        # if record[1] == 'LOCATION':
        #     continue
        if record[1] == LOCATION:
            LOCATION_FOUND = True
            if record[0] == DATE:
                # print(record)
                MIN_TEMP = float(record[2])
                MAX_TEMP = float(record[3])
            if record[2] != 'NA':
                AVG_MIN += float(record[2])
            if record[3] != 'NA':
                AVG_MAX += float(record[3])
        if WEATHER.get(record[1]) is None:
            WEATHER[record[1]] = []
        WEATHER[record[1]].append(record)
if not LOCATION_FOUND:
    print("Invalid Input")
    exit()

AVG_MIN /= len(WEATHER[LOCATION])
AVG_MAX /= len(WEATHER[LOCATION])

def a_or_b(one, two):
    '''
    Checks if a is larger than b and if so, returns 'below'
        otherwise returns 'above'
    '''
    if one <= two:
        return 'below'
    return 'above'

def diff(one, two):
    '''
    Makes final print statements shorter
    takes care of finding the difference,
    making it absolute and rounding to 1 d.p.
    '''
    return round(fabs(one-two), 1)

# print(MIN_TEMP)
# print(MAX_TEMP)
# print(AVG_MIN)
# print(AVG_MAX)

print(f"MinTemp is {diff(AVG_MIN, MIN_TEMP)} degrees {a_or_b(MIN_TEMP, AVG_MIN)} average minimum")
print(f"MaxTemp is {diff(AVG_MAX, MAX_TEMP)} degrees {a_or_b(MAX_TEMP, AVG_MAX)} average maximum")
