#!/usr/bin/python  
# -*- coding: utf-8 -*-
import os
import time

def main():
    print('days in 2018 06 19 = ', get_days_from_date(year=2018, month=6, day=19))

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def get_days_from_date(year, month, day):
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if is_leap_year(year):
        months[2]=29
    sum = day
    for i in range(1,month+1):
        print('i:',i)
        sum += months.get(i)
    return sum

if __name__ == '__main__':
    main() 