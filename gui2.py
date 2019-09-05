#!/usr/local/bin/python3

from tkinter import *

window  = Tk()
window.title("Working With Labels")
#window.geometry("400x400")
window.minsize(width=300, height=300)
window.maxsize(height=500, width=500)


lbl1 = Label(window, text="Hello", font = ("Arial Bold", 20))
lbl2 = Label(window, text="    ")
lbl3 = Label(window, text="GBye")
lbl4 = Label(window, text="   ")
lbl5 = Label(window, text="Here")

lbl1.grid(column = 0, row = 0)
lbl2.grid(column = 1, row = 0)
lbl3.grid(column = 2, row = 0)
lbl4.grid(column = 0, row = 1)
lbl5.grid(column = 1, row = 1)


window.mainloop()

