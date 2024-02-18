import validators
from customtkinter import filedialog

def choose_folder(entry_folder):
    folder = filedialog.askdirectory()
    entry_folder.configure(state='normal')
    entry_folder.insert(0, folder)
    entry_folder.configure(state='disabled')