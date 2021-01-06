from tkinter import *
import backend

window = Tk()

################
# FUNCTIONS ####
################

def get_selected_row (event):
    try:
        global selected_tuple
        index = listbox.curselection()[0]
        selected_tuple = listbox.get(index)
        display_values()
        return selected_tuple
    except IndexError:
        pass

def clear_insert_values():
    what_entry.delete(0,END)
    when_entry.delete(0,END)
    cost_entry.delete(0, END)
    who_entry.delete(0, END)

def display_values():
    clear_insert_values()
    what_entry.insert(END,selected_tuple[1])
    when_entry.insert(END,selected_tuple[2])
    cost_entry.insert(END,selected_tuple[3])
    who_entry.insert(END,selected_tuple[4])

def view_command():
    listbox.delete(0, END) #Tar bort alla gamla records
    for el in backend.view():
        listbox.insert(END, el) #Nya inserts blir på slutet av listan



def search_command():
    listbox.delete(0, END)
    for el in backend.search(what_val.get(), when_val.get(), cost_val.get(), who_val.get()): #Vi måste använda .get() eftersom de är stringvars och inte string
        listbox.insert(END,el)

def insert_command():
    if (who_val.get() == 'C' or who_val.get() == 'c' or who_val.get() == 'L' or who_val.get() == 'l') and len(what_val.get()) != 0:
        listbox.delete(0, END)
        backend.insert(what_val.get(), when_val.get(), cost_val.get(), who_val.get())
        update_values()
        view_command()
    else:
        pass

def update_command():
    backend.update(selected_tuple[0], what_val.get(), when_val.get(), cost_val.get(), who_val.get())
    update_values()
    view_command()


def delete_command():
    backend.delete(selected_tuple[0])
    update_values()
    view_command()
     # Fylla i selected value till rutorna vet ej
     # Ta bort recorden från databasen

# Listbox & Scroller
listbox = Listbox(window, height = 6, width = 35)
listbox.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)
scroll = Scrollbar(window)
scroll.grid(row = 2, column = 2, rowspan = 6)
listbox.configure(yscrollcommand = scroll.set)
scroll.configure(command = listbox.yview)
listbox.bind('<<ListboxSelect>>', get_selected_row) # väljer den raden användaren trycker på

def calles_expenses():
    holder = 0
    database = backend.c_costs()
    for el in database:
        holder += el[3]
    return holder

def linus_expenses():
    holder = 0
    database = backend.l_costs()
    for el in database:
        holder += el[3]
    return holder


#################
# FUNCTIONS END #
#################

################
# GUI ##########
################

# Labels (texts)
what_text = Label(window, text = "What:")
what_text.grid(row = 0, column = 0)
cost_text = Label(window, text = "Cost:")
cost_text.grid(row = 0, column = 2)
when_text = Label(window, text = "When:")
when_text.grid(row = 1, column = 0)
who_text = Label(window, text = "Who (C or L):")
who_text.grid(row = 1, column = 2)

def update_values():
    calle_paid = Label(window, text = f"Calle has paid: {calles_expenses()} ")
    calle_paid.grid(row = 8, column = 0)
    linus_paid = Label(window, text = f"Linus has paid: {linus_expenses()} ")
    linus_paid.grid(row = 9, column = 0)

def delete_recent_entry():
    backend.delete_latest()
    update_values()
    view_command()


#NOT ADDED: ADD BETALAT LABELS

# Entries
what_val = StringVar()
what_entry = Entry(window, textvariable = what_val)
what_entry.grid(row = 0, column = 1)
cost_val = StringVar()
cost_entry = Entry(window, textvariable = cost_val)
cost_entry.grid(row = 0, column = 3)
when_val = StringVar()
when_entry = Entry(window, textvariable = when_val)
when_entry.grid(row = 1, column = 1)
who_val = StringVar()
who_entry = Entry(window, textvariable = who_val)
who_entry.grid(row = 1, column = 3)

# Listbox & Scroller
listbox = Listbox(window, height = 6, width = 35)
listbox.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)
scroll = Scrollbar(window)
scroll.grid(row = 2, column = 2, rowspan = 6)
listbox.configure(yscrollcommand = scroll.set)
scroll.configure(command = listbox.yview)
listbox.bind('<<ListboxSelect>>', get_selected_row) # väljer den raden användaren trycker på

# Buttons
b1 = Button(window, text = "View All", width = 12, command = view_command)
b1.grid(row = 2, column = 3)
b2 = Button(window, text = "Add", width = 12, command = insert_command)
b2.grid(row = 4, column = 3)
b3 = Button(window, text = "Remove", width = 12, command = delete_command)
b3.grid(row = 6, column = 3)
b4 = Button(window, text = "Update", width = 12, command = update_command)
b4.grid(row = 5, column = 3)
b5 = Button(window, text = "Search", width = 12, command = search_command)
b5.grid(row = 3, column = 3)
b6 = Button(window, text = "Remove Last", width = 12, command = delete_recent_entry)
b6.grid(row = 7, column = 3)
b7 = Button(window, text = "Close", width = 12, command = window.destroy)
b7.grid(row = 8, column = 3)


################
# GUI END ######
################
view_command() # Visa allting direkt
update_values()
window.wm_title("Råholmsvägen expenses")
window.mainloop()