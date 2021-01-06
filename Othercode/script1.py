from tkinter import * 

window = Tk()

def calc ():
    num1 = float(e1_value.get())
    num2 = float(e2_value.get())
    multi = num1*num2
    #res = "The result of the multiplication is: " + num1*num2
    #print(res)
    t1.insert(END, res)


b1 = Button(window, text = "Calculate", command = calc)
b1.grid(row = 0, column = 0)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value)
e2.grid(row = 0, column = 2)


t1 = Text(window, height = 1, width = 10) #Height är i cells
t1.grid(row = 0, column = 3)



window.mainloop()