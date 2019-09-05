#!/usr/local/bin/python3

from tkinter import *

window = Tk()
window.geometry('400x400')
window.title("Dem Texty Grills")

lbl1 = Label(window, text = "Please click button")
lbl1.grid(column = 0 , row = 0)

txtVar1 = StringVar()
txt1 = Entry (window, width = 10 , textvariable = txtVar1)

#txt1 = Entry(window, width = 10, state = "disabled")
txt1.grid(column = 1 , row = 0)
txt1.focus()

def hasClicked() :
    msg = "Something happened to " + txtVar1.get()
    txtVar1.set(" ")
    lbl1.configure(text = msg)

btn1 = Button(window, text = "Sumbit", command = hasClicked)
btn1.grid(column = 0, row = 2) 

window.mainloop()