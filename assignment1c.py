#!/usr/local/bin/python3

input1 = input("Please enter a number")
input2 = input("Please enter another number")



def addThem(temp1,temp2):
    temp3 = temp1 + temp2
    return temp3

def subThem(temp1,temp2):
    temp3 = temp1 - temp2
    return temp3

def mulThem(temp1,temp2):
    temp3 = temp1 * temp2
    return temp3

def divThem(temp1,temp2):
    temp3 = temp1 / temp2
    return temp3


if (input1.isnumeric() and input2.isnumeric()):
    

    input1 = float(input1)
    input2 = float(input2)

    x = addThem(input1,input2)
    print("%f + %f = %f" %(input1, input2, x))

    x = subThem(input1,input2)
    print("%f + %f = %f" %(input1, input2, x))

    x = mulThem(input1,input2)
    print("%f + %f = %f" %(input1, input2, x))
    
    x = divThem(input1,input2)
    print("%f + %f = %f" %(input1, input2, x))

else :

    print("Please enter numbers")