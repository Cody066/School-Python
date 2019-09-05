#!/usr/local/bin/python3

from tkinter import *

window = Tk()
window.geometry('400x400')
window.title("Dem Butt-ons")

lbl1 = Label(window, text = "Please click button")
lbl1.grid(column = 0 , row = 0)

#define the hasClicked function, same as actionPerformed from Java
def hasClicked() :
    lbl1.configure(text = "Something happened")

#JButton = new JButton ("Submit")

btn1 = Button(window, text = "Sumbit", command = hasClicked)
btn1.grid(column = 0, row = 2) 



window.mainloop()