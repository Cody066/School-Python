#!/usr/local/bin/python3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.geometry('700x400')
window.title("Pizza")



lbl1 = Label(window, text = "Please select your size and toppings")
lbl1.grid(column = 0 , row = 0)

lbl2 = Label(window, text = "")
lbl2.grid(column = 0 , row = 9)

size = ("SML", "MED", "LG", "XLG")
select1 = ttk.Combobox(window, values = size, width = 20)
select1.current(0)
select1.grid(column = 2, row = 2)

pepVar = StringVar()
pep = Checkbutton(window, text = "Pepperoni", variable = pepVar)
pep.grid(column = 1 , row = 4)

cheeseVar = StringVar()
cheese = Checkbutton(window, text = "Cheese", variable = cheeseVar)
cheese.grid(column = 1 , row = 5)

oliveVar = StringVar()
olive = Checkbutton(window, text = "Olive", variable = oliveVar)
olive.grid(column = 1 , row = 6)

pineVar = StringVar()
pine = Checkbutton(window, text = "Pineapple", variable = pineVar)
pine.grid(column = 1 , row = 7)

hamVar = StringVar()
ham = Checkbutton(window, text = "Ham", variable = hamVar)
ham.grid(column = 1 , row = 8)

def hasClicked():

    total = 0.0

    if (select1.get() == "SML") :
        total = 9.00 
    elif (select1.get() == "MED") :
        total = 12.50   
    elif (select1.get() == "LG") :
        total = 15.00  
    elif (select1.get() == "XLG") :
        total = 17.50           

    msg = " Size : " + select1.get() + "\n Toppings :"

    if (pepVar.get()) :
       total += 1
       msg += " Pepperoni"

    if (cheeseVar.get()):
        msg += " Cheese"

    if (oliveVar.get()):
        total += 1
        msg += " Olives"

    if (pineVar.get()) :
        total += 1
        msg += " Pineapple"

    if (hamVar.get()):
        total += 1
        msg += " Ham "

    msg += "\n Total : %0.2f" %(total)
    
    #lbl2.configure(text = msg) 

    messagebox.showinfo("Order", msg)



btn1 = Button(window, text = "Submit", command = hasClicked)
btn1.grid(column = 0, row = 2) 


window.mainloop()