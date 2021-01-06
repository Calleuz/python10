from tkinter import *

window = Tk()

def add ():
    num1 = float(e1_val.get())
    num2 = float(e2_val.get())
    res = num1+num2
    t1.delete("1.0", END)
    t1.insert(END, " ")
    t1.insert(END, res)
def subtract ():
    num1 = float(e1_val.get())
    num2 = float(e2_val.get())
    res = num1-num2
    t1.delete("1.0", END)
    t1.insert(END, " ")
    t1.insert(END, res)
def multiply ():
    num1 = float(e1_val.get())
    num2 = float(e2_val.get())
    res = num1*num2
    t1.delete("1.0", END)
    t1.insert(END, " ")
    t1.insert(END, res)
def divide ():
    num1 = float(e1_val.get())
    num2 = float(e2_val.get())
    res = num1/num2
    t1.delete("1.0", END)
    t1.insert(END, " ")
    t1.insert(END, res)

b1 = Button(window, text = "Add", command = add)
b1.grid(row = 1, column = 0)
b2 = Button(window, text = "Subtract", command = subtract)
b2.grid(row = 1, column = 1)
b3 = Button(window, text = "Multiply", command = multiply)
b3.grid(row = 2, column = 0)
b4 = Button(window, text = "Divide", command = divide)
b4.grid(row = 2, column = 1)

e1_val = StringVar()
e1 = Entry(window, textvariable = e1_val)
e1.grid(row = 0, column = 0)

e2_val = StringVar()
e2 = Entry(window, textvariable = e2_val)
e2.grid(row = 0, column = 1)

t1 = Text(window, height = 1, width = 26)
t1.grid(row = 3, column = 0, rowspan = 2)



window.mainloop()