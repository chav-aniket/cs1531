from datetime import date, time, datetime
from timetable import *

def test_one():
    '''
    Same days, different years
    '''
    dates_one = [date(2019,12,25), date(2020,12,25), date(2018,12,25)]
    times_one = [time(12,30)]
    ans = [datetime(2018,12,25,12,30),datetime(2019,12,25,12,30),datetime(2020,12,25,12,30)]
    assert timetable(dates_one,times_one) == ans

def test_two():
    '''
    Time sorting test
    '''
    dates_two = [date(2020,2,2)]
    times_two = [time(13,30),time(6,50),time(22,0)]
    ans = [datetime(2020,2,2,6,50),datetime(2020,2,2,13,30),datetime(2020,2,2,22,0)]
    assert timetable(dates_two,times_two) == ans

def test_three():
    '''
    Duplicate dates test
    '''
    dates_three = [date(2000,11,8),date(2000,11,7),date(2000,11,8)]
    times_three = [time(12,50)]
    ans = [datetime(2000,11,7,12,50),datetime(2000,11,8,12,50),datetime(2000,11,8,12,50)]
    assert timetable(dates_three,times_three) == ans

def test_four():
    '''
    Duplicate times test
    '''
    dates_four = [date(2016,7,3)]
    times_four = [time(13,0),time(13,0),time(1,55)]
    ans = [datetime(2016,7,3,1,55),datetime(2016,7,3,13,0),datetime(2016,7,3,13,0)]
    assert timetable(dates_four,times_four) == ans

def test_five():
    '''
    Test included in documentation 
    '''
    dates_five = [date(2019,9,27), date(2019,9,30)]
    times_five = [time(14,10), time(10,30)]
    ans = [datetime(2019,9,27,10,30), datetime(2019,9,27,14,10), datetime(2019,9,30,10,30), datetime(2019,9,30,14,10)]
    assert timetable(dates_five,times_five) == ans