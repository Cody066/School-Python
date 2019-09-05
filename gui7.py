#!/usr/local/bin/python3

from tkinter import *

window = Tk()
window.geometry('400x400')
window.title("Dem Radio Butt-ons")

def hasClicked() :
    msg = " You have selected : " + sel1.get()
   # lbl1.configure(text = msg) 

    from tkinter import messagebox
    messagebox.showinfo("Info", msg)

    fav = messagebox.askquestion("Really ?", "You sure bout dat ?")
    lbl1.configure(text = fav)

sel1 = StringVar()

radbut1 = Radiobutton(window, text = "Car", value = "1", variable =  sel1)
radbut2 = Radiobutton(window, text = "Dog", value = "2", variable =  sel1)
radbut3 = Radiobutton(window, text = "Cat", value = "3", variable =  sel1)

radbut1.grid(column = 3, row = 2)
radbut2.grid(column = 3, row = 4)
radbut3.grid(column = 3, row = 6)


lbl1 = Label(window, text = "Please click button")
lbl1.grid(column = 0 , row = 0)

btn1 = Button(window, text = "Sumbit", command = hasClicked)
btn1.grid(column = 0, row = 2) 

window.mainloop()