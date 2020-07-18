# https://www.hackerrank.com/challenges/python-time-delta/problem


from datetime import datetime, date, time, timedelta
#from collections import namedtuple

t1 = 'Sun 10 May 2015 13:54:36 -0700'
t2 = 'Sun 10 May 2015 13:54:36 -0000'
t3 = 'Sat 02 May 2015 19:54:36 +0530'
t4 = 'Fri 01 May 2453 13:54:36 -0000'

#Datestr = namedtuple('Datestr', ['weekday', 'day', 'month', 'year', 'time', 'tzone'])


def time_delta(t1: str, t2: str):
    d1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    d2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    delta = abs(d1 - d2)
    return str(int(delta.total_seconds()))

    # don't do any of this.
    
    #monthmap = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May':5, 'Jun':6,
    #             'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    #date1 = Datestr(*t1.split(" "))
    #date2 = Datestr(*t2.split(" "))
    #date1 = t1.split(); date2 = t2.split()
    #date1str = '' + date1[1] + str(monthmap[date1[2]]) + date[3]
    #dt1 = datetime()

time_delta(t3, t4)
    