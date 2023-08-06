import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

class SorterInterface(tk.Tk):
    def __init__(self):
        # atribute for the object
        self.path = 'home'
        
        # window created
        super().__init__()
        self.title('Files Sorter')
        self.geometry('300x300')
        
        self.create_widget()
        
        
        # running windows
        self.mainloop()
        
    def create_widget(self):
        ttk.Button(self, text='Select Directory' , command= lambda : self.select_path()).pack(pady=5)
        self.path_label = ttk.Label(self)
        self.path_label.pack(pady=5)
        ttk.Button(self, text='Sort', command= lambda : self.sort_file()).pack(pady=5)
        
    # get the directory path
    def select_path(self):
        self.path = fd.askdirectory()
        self.path_label.config(text=self.path)
        
        
        
    # run the sorting system
    def sort_file(self):
        print('run')
        
sorter = SorterInterface()
# sorter.mainloop()