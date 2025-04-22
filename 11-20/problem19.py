#! /usr/bin/python

# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# function for checking a leap year
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# creating a dictionary for months and their number of days
months = { "January": 31,
        "February" : 28,
        "March" : 31,
        "April" : 30,
        "May" : 31,
        "June" : 30,
        "July" : 31,
        "August" : 31,
        "September" : 30,
        "October" : 31,
        "November" : 30,
        "December" : 31}

sunday_counter = 0
day  = 2 # started from 2 since 01/01/1901 was a Tuesday. Sunday is 0 in this case
for year in range(1901,2001):
    for m in months:
        if day%7 == 0:
            sunday_counter += 1
        day_in_month = months[m]
        if m == 'February' and is_leap(year):
            day_in_month += 1
        day += (months[m])

print("Total Sundays are: ", sunday_counter)

