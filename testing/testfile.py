import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.tkscrollbarhelper import TkScrollbarHelper


class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        self.top_level = tk.Frame(master)
        self.preview_button = tk.Button(self.top_level)
        self.preview_button.config(cursor='draft_large', text='Preview task')
        self.preview_button.place(anchor='nw', x='0', y='0')
        self.create_button = tk.Button(self.top_level)
        self.create_button.config(text='Create task')
        self.create_button.grid(column='1', row='0')
        self.task_title = tk.Entry(self.top_level)
        self.task_title.config(font='TkDefaultFont', relief='sunken', takefocus=False)
        _text_ = '''task title text'''
        self.task_title.delete('0', 'end')
        self.task_title.insert('0', _text_)
        self.task_title.grid(column='0', columnspan='3', row='1', sticky='w')
        self.task_description = tk.Text(self.top_level)
        self.task_description.config(height='10', insertunfocussed='hollow', width='30')
        _text_ = '''Task description area'''
        self.task_description.insert('0.0', _text_)
        self.task_description.grid(column='0', columnspan='2', row='2')

        
        self.listbox_1 = tk.Listbox(self.top_level)
        self.listbox_1.config(activestyle='underline', exportselection='true', font='TkDefaultFont', selectmode='extended')
        self.listbox_1.config(setgrid='false', state='disabled', takefocus=True)
        self.listbox_1.grid(column='2', columnspan='2', row='2')
 
        self.sb1 = tk.Scrollbar(self.top_level)
        self.sb1.grid(row = 2, column = 4, rowspan = 6)
 
        self.listbox_1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.listbox_1.yview)


        self.search_entry = tk.Entry(self.top_level)
        self.search_entry.config(relief='raised')
        _text_ = '''Search category'''
        self.search_entry.delete('0', 'end')
        self.search_entry.insert('0', _text_)
        self.search_entry.grid(column='3', row='0')
        self.use_button = tk.Button(self.top_level)
        self.use_button.config(text='<- Use selected task')
        self.use_button.grid(column='2', row='1')
        self.view_button = tk.Button(self.top_level)
        self.view_button.config(text='View all')
        self.view_button.grid(column='3', row='1')
        self.top_level.config(height='200', width='200')
        self.top_level.grid()

        # Main widget
        self.mainwindow = self.top_level


    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    app = NewprojectApp(root)
    app.run()

