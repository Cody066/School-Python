#!/usr/local/bin/python3

from datetime import datetime
from datetime import date 

inputTime1 = input("Please enter a date YYYY-MM-DD")
inputTime2 = datetime.strptime(inputTime1, '%Y-%m-%d')

dateA = (inputTime2)
dateB = datetime(2018,6,30)

daysCount = dateA - dateB
 
print(daysCount.days)









