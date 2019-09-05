#!/usr/local/bin/python3

from tkinter import *

window = Tk()
window.geometry('400x400')
window.title("Enter Grades")

lbl1 = Label(window, text = "Enter Grade")
lbl1.grid(column = 0 , row = 0)

lbl2 = Label(window, text = "")
lbl2.grid(column = 0 , row = 4)

txtVar1 = StringVar()
txt1 = Entry (window, width = 10 , textvariable = txtVar1)

#txt1 = Entry(window, width = 10, state = "disabled")
txt1.grid(column = 1 , row = 0)
txt1.focus()

def hasClicked() :
    
    newVar = txtVar1.get()
    
    if (newVar != ""):
        try:
            (float(newVar))
            if (float(newVar) >= 85.0 ) :
                msg = "A"
            elif(float(newVar) >= 75.0 and float(newVar) <= 84.99) :
                msg = "B"
            elif(float(newVar) >= 60.0 and float(newVar) <= 74.99) :
                msg = "C"
            elif(float(newVar) < 59.99) :
                msg = "F" 
            else:msg = "Please enter a grade" 
                
        except:
        
            if (str(newVar) == "A" or str(newVar) == "a") :
                msg = "85-100"
            elif (str(newVar) == "B" or str(newVar) == "b") :
                msg = "75-84.99"
            elif(str(newVar) == "C" or str(newVar) == "c") :
                msg = "60-74.99"
            elif(str(newVar) == "D" or str(newVar) == "d") :
                msg = "0-59.99"  
            else:msg = "Please enter a grade"

        lbl2.configure(text = msg, font = ("Arial",12), fg= "black")

    else : 
        msg = "Please enter a grade a proper format"
        lbl2.configure(text = msg, font = ("Arial Bold",12), fg= "red")
                        
    lbl2.configure(text = msg) 



btn1 = Button(window, text = "Enter", command = hasClicked)
btn1.grid(column = 0, row = 2) 

window.mainloop()