#!/usr/local/bin/python3

from tkinter import *

window = Tk()
window.geometry('400x400')
window.title("Check out the box")

lbl1 = Label(window, text = "Please check a box and click a button")
lbl1.grid(column = 0 , row = 0)

checkVar1 = StringVar()
check1 = Checkbutton(window, text = "Car", variable = checkVar1)
check1.grid(column = 2 , row = 2)

checkVar2 = StringVar()
check2 = Checkbutton(window, text = "Dog", variable = checkVar2)
check2.grid(column = 2 , row = 4)

checkVar3 = StringVar()
check3 = Checkbutton(window, text = "Cat", variable = checkVar3)
check3.grid(column = 2 , row = 6)

def hasClicked() :
    msg = "C1 : " + checkVar1.get()
    msg += ", C2 : " + checkVar2.get()
    msg += ", C3 : " + checkVar3.get()
    lbl1.configure(text = msg) 

btn1 = Button(window, text = "Sumbit", command = hasClicked)
btn1.grid(column = 0, row = 2) 


window.mainloop()