#!/usr/local/bin/python3
import math

myInput = input('Enter a Number')

if (str.isdigit(myInput)) :
    num = float(myInput)
    num1 = math.ceil(num)
    num2 = math.floor(num1) 
    num3 = round(num2)
    print ("You entered %f" %(num3))
  
else :
    myInput = input('Enter a Number PLEASE')