#!/usr/local/bin/python3

from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('400x400')
window.title("Working with Select Workers")

lbl1 = Label(window, text = "Please click button")
lbl1.grid(column = 0 , row = 0)

number = ("Choose a Number", 1,2,"Three", "Four", 5)
select1 = ttk.Combobox(window, values = number, width = 20)
select1.current(0)
select1.grid(column = 2, row = 2)

def hasClicked() :
    msg = "I selected : " + select1.get()
    lbl1.configure(text = msg) 
    
btn1 = Button(window, text = "Sumbit", command = hasClicked)
btn1.grid(column = 0, row = 2) 



window.mainloop()