from datetime import date, time, datetime

def timetable(dates, times):
    '''
    Generates a list of datetimes given a list of dates and a list of times. 
    All possible combinations of date and time are contained within the result. 
    The result is sorted in chronological order.

    For example,
    >>> timetable([date(2019,9,27), date(2019,9,30)], [time(14,10), time(10,30)])
    [datetime(2019,9,27,10,30), datetime(2019,9,27,14,10), datetime(2019,9,30,10,30), datetime(2019,9,30,14,10)]
    '''
    ret = []
    for x in dates:
        for y in times:
            new = datetime(x.year, x.month, x.day, y.hour, y.minute)
            ret.append(new)

    return sorted(ret)