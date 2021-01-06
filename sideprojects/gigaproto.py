import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from gigabackend import Database

db = Database("tasks.db")

class NotreadyApp:



    def __init__(self, master=None):
        # build ui
        self.window = tk.Frame(master)

        # self.preview_button = tk.Button(self.window, command = self.preview_command)
        # self.preview_button.config(text='Preview task')
        # self.preview_button.grid(sticky='w')
        self.create_button = tk.Button(self.window, command = self.add_command)
        self.create_button.config(cursor='bottom_left_corner', text='Submit task')
        self.create_button.grid(column='0', row='0', sticky='e')
        self.use_button = tk.Button(self.window, command = self.display_values)
        self.use_button.config(text='<- Use selected task')
        self.use_button.grid(column='2', row='0')
        self.view_button = tk.Button(self.window, command = self.view_command)
        self.view_button.config(text='View all')
        self.view_button.grid(column='3', row='0')
        self.delete_button = tk.Button(self.window, command = self.delete_command)
        self.delete_button.config(text = "Delete most recent")
        self.delete_button.grid(column="2", row = "1")
        self.search_button = tk.Button(self.window, command = self.search_command)
        self.search_button.config(text = "Search")
        self.search_button.grid(column = '4', row = '1')

        self.e1_text = StringVar()
        self.entry_1 = tk.Entry(self.window, textvariable = self.e1_text)
        _text_ = '''Enter task title'''
        self.entry_1.delete('0', 'end')
        self.entry_1.insert('0', _text_)
        self.entry_1.grid(column='0', row='1', sticky='w')

        self.e2_text = StringVar()
        self.entry_2 = tk.Entry(self.window, textvariable = self.e2_text)
        _text_ = '''Search premade tasks'''
        self.entry_2.delete('0', 'end')
        self.entry_2.insert('0', _text_)
        self.entry_2.grid(column='2', row='2')

        self.text_1 = tk.Text(self.window)#, textvariable = self.text_entry)
        self.text_1.config(height='10', width='30')
        _text_ = '''Enter task description'''
        self.text_1.insert('0.0', _text_)
        self.text_1.grid(column='0', row='3')

        self.e3_text = StringVar()
        self.entry_3 = tk.Entry(self.window, textvariable = self.e3_text)
        _text_ = '''Enter task category'''
        self.entry_3.delete('0', 'end')
        self.entry_3.insert('0', _text_)
        self.entry_3.grid(column='0', row='2', sticky='w')
        self.list1 = tk.Listbox(self.window)
        self.list1.grid(column='2', row='3')
        self.window.config(height='200', width='200')
        self.window.grid()

        self.sb1=tk.Scrollbar(self.window)
        self.sb1.grid(row=3,column=3,rowspan=6)
 
        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)


        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)


        # Main widget
        self.mainwindow = self.window

    def add_command(self):
        global text_content 
        text_content = self.text_1.get("1.0",END)
        db.insert(self.e1_text.get(), self.e3_text.get(), text_content)
        self.view_command()
        #self.clear_insert_values()

    def preview_command(self):
        print("Preview")
    
    def view_command(self):
        self.list1.delete(0,END)
        for el in db.view():
            self.list1.insert(END, el)
    
    def use_command(self):
        pass


    def delete_command(self):
        db.delete_latest()
        self.view_command()
    
    def get_selected_row(self, event):
        try:
            global selected_tuple
            self.index = self.list1.curselection()[0]
            selected_tuple = self.list1.get(self.index)
            #self.display_values()
            print(selected_tuple)
            return selected_tuple
        except IndexError:
            pass
    

    def clear_insert_values(self):
        self.entry_1.delete(0,END)
        self.entry_3.delete(0,END)
        self.text_1.delete("1.0", "end")



    def display_values(self):
        self.clear_insert_values()
        self.entry_1.insert(END,selected_tuple[1])
        self.entry_3.insert(END,selected_tuple[2])
        self.text_1.insert(END,selected_tuple[3])


    def run(self):
        self.mainwindow.mainloop()
    
    def search_command(self):
        self.clear_insert_values()
        res = db.search(self.e1_text.get(), self.e3_text.get(), self.text_1.get())
        for el in res:
            self.list1.insert(END, el)



if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    app = NotreadyApp(root)
    app.run()

