#!/usr/bin/python3
#Print the calendar of a given month and year

import calendar
year=int(input("Please enter the year: "))
month=int(input("Please enter the month: "))
print(calendar.month(year,month))
