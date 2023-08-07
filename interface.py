import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from pathlib import Path
import shutil, os, copy

class SorterInterface(tk.Tk):
    def __init__(self):
        # atribute for the object
        self.path = 'home'
        
        # window created
        super().__init__()
        self.title('Files Sorter')
        self.geometry(self.middle_cordinate(window_width=400,window_height=300))
        
        self.create_widget()
        
        
        # running windows
        self.mainloop()
        
    def create_widget(self):
        ttk.Button(self, text='Select Directory' , command= lambda : self.select_path()).pack(pady=5)
        self.path_label = ttk.Label(self, text='home')
        self.path_label.pack(pady=5)
        ttk.Button(self, text='Sort', command= lambda : self.sort_file()).pack(pady=5)
    
    def middle_cordinate(self,window_width, window_height):
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        
        # // to get integer output so it's valid for geometry size
        x = (screen_w - window_width) //2
        y = (screen_h - window_height)//2
        
        return f'{window_width}x{window_height}+{x}+{y}'
    
    # get the directory path
    def select_path(self):
        self.path = fd.askdirectory()
        self.path_label.config(text=self.path)
        
       
    def check_exist_file(self, file_name, destination_folder, i = ''):
        # save original file name list
        original_file_name = copy.copy(file_name)
        
        # change filename (example : example.txt -> example1.txt)
        temp = file_name[-2]
        file_name[-2] = f'{temp}{i}'
        temp_file_name = '.'.join(file_name)
        
        # create path with the new file name (example:  desktop/example1.txt)
        new_path = Path(destination_folder)/Path(temp_file_name)
        
        # check if path already exist
        if new_path.is_file() :
            i = 1 if i == '' else i+1
            # change file name again if file name already exist
            new_path = self.check_exist_file(original_file_name,destination_folder,i)

        # return if the new file name not exist
        return new_path
        
    # run the sorting system
    def sort_file(self):
        # return list of file name
        list_directory = os.listdir(self.path)
        
        for item in list_directory:
            file_name =  item.split('.')
            
            # check if item is not a folder
            if len(file_name) == 1:
                continue
            
            # get file extension
            file_extension = file_name[-1]
            
            # check the extension already have a folder
            extension_folder = Path(self.path)/Path(file_extension)
            if not extension_folder.is_dir() :
                # create extension folder
                os.mkdir(path=extension_folder)
            
            # check if file already exist in extension folder
            destination = self.check_exist_file(file_name,extension_folder)
            
            # copy file to it's extension folder
            file_path = Path(self.path)/Path(item)
            shutil.move(file_path, destination)
            
            
        
sorter = SorterInterface()
# sorter.mainloop()