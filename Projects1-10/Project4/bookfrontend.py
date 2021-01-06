from tkinter import *
import bookbackend

window = Tk()


def get_selected_row (event):
    if listbox.size() == 0:
        pass # I detta fallet kan man också använda try: / except Indexerror: pass
    global selected_tuple #Vi definierar den som global eftersom vi då inte behöver calla get_selected_row med en parameter
    index = listbox.curselection()[0]
    selected_tuple = listbox.get(index)
    display_values()
    return selected_tuple

def clear_insert_values():
    title.delete(0,END)
    author.delete(0,END)
    year.delete(0, END)
    ISBN.delete(0, END)

def display_values():
    clear_insert_values()
    title.insert(END,selected_tuple[1])
    author.insert(END,selected_tuple[2])
    year.insert(END,selected_tuple[3])
    ISBN.insert(END,selected_tuple[4])



def view_command():
    listbox.delete(0, END) #Tar bort alla gamla records
    for el in bookbackend.view():
        listbox.insert(END, el) #Nya inserts blir på slutet av listan


def search_command():
    listbox.delete(0, END)
    for el in bookbackend.search(title_val.get(), author_val.get(), year_val.get(), ISBN_val.get()): #Vi måste använda .get() eftersom de är stringvars och inte string
        listbox.insert(END,el)

def insert_command():
    listbox.delete(0, END)
    bookbackend.insert(title_val.get(), author_val.get(), year_val.get(), ISBN_val.get())
    #listbox.insert(END, "Your book was added successfully!")
    view_command()

def update_command():
    bookbackend.update(selected_tuple[0], title_val.get(), author_val.get(), year_val.get(), ISBN_val.get())
    view_command()


def delete_command():
    bookbackend.delete(selected_tuple[0])
    view_command()
     # Fylla i selected value till rutorna vet ej
     # Ta bort recorden från databasen



title_label = Label(window, text = "Title")
title_label.grid(row = 0, column = 0)

year_label = Label(window, text = "Year")
year_label.grid(row = 1, column = 0)

author_label = Label(window, text = "Author")
author_label.grid(row = 0, column = 2)

ISBN_label = Label(window, text = "ISBN")
ISBN_label.grid(row = 1, column = 2)

title_val = StringVar()
title = Entry(window, textvariable = title_val)
title.grid(row = 0, column = 1)

year_val = StringVar()
year = Entry(window, textvariable = year_val)
year.grid(row = 1, column = 1)

author_val = StringVar()
author = Entry(window, textvariable = author_val)
author.grid(row = 0, column = 3)

ISBN_val = StringVar()
ISBN = Entry(window, textvariable = ISBN_val)
ISBN.grid(row = 1, column = 3)

listbox = Listbox(window, height = 6, width = 35)
listbox.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)


scroll = Scrollbar(window)
scroll.grid(row = 2, column = 2, rowspan = 6)

listbox.configure(yscrollcommand = scroll.set)
scroll.configure(command = listbox.yview)
listbox.bind('<<ListboxSelect>>', get_selected_row) # väljer den raden användaren trycker på 


# def view():
#     print("viewing all")
# def search():
#     print("Searching")
# def add():
#     print("Adding entry")
# def update():
#     print("updating")
# def delete():
#     print("Deleting")
# def close():
#     print("closing")

b1 = Button(window, text = "View All", width = 12, command = view_command)
b1.grid(row = 2, column = 3)
b2 = Button(window, text = "Search Entry", width = 12, command = search_command)
b2.grid(row = 3, column = 3)
b3 = Button(window, text = "Add Entry", width = 12, command = insert_command)
b3.grid(row = 4, column = 3)
b4 = Button(window, text = "Update", width = 12, command = update_command)
b4.grid(row = 5, column = 3)
b5 = Button(window, text = "Delete", width = 12, command = delete_command)
b5.grid(row = 6, column = 3)
b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)


window.wm_title("Book Store")




window.mainloop()