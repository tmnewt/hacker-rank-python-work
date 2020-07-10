# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar

m, d, y = list(map(int, input().split()))
calendar.setfirstweekday(firstweekday=6)
days = list(calendar.day_name)
print(days[calendar.weekday(y, m, d)].upper())
#print(calendar.TextCalendar(firstweekday=-1).formatyear(2020))

