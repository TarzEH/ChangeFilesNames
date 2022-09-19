import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


def select_files():
    filetypes = (
        ('All files', '*.*'),
        ('text files', '*.txt')

    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    return filenames


def select_dir():
    dirname = fd.askdirectory()
    return dirname

def run():
    # create the root window
    root = tk.Tk()
    root.title('Change files name app')
    root.resizable(False, False)
    root.geometry('300x150')

    # open buttons
    open_button = ttk.Button(
        root,
        text='Open Files',
        command=select_files
    )
    open_button2 = ttk.Button(
        root,
        text='Open Dirs',
        command=select_dir
    )

    open_button.pack(expand=True)
    open_button2.pack(expand=True)

    root.mainloop()
