import os
from tkinter import *


#Functions
def condition_function(filename):
    new_file=os.path.basename(os.path.normpath(filename))
    if os.path.isfile(filename) and new_file != ".DS_Store":
        new_file=new_file.replace(" ", "")
        new_file=new_file.replace("@", "")
        new_file=new_file.replace("!", "")
        new_file=new_file.replace("#", "")
        new_file=new_file.replace("%", "")
        new_file=new_file.replace("$", "")
        new_file=new_file.replace("/", "")
        new_file = new_file.replace(":", "")
        os.rename(filename, new_file)
        return;





#Program
def Program(dir):
    os.chdir(dir)
    directory=os.path.basename(os.path.normpath(dir))
    path=os.walk(os.getcwd())
    for root, directories, files in path:
            for file in os.listdir(root):
                full_path = os.path.join(root, file)
                #if os.path.isfile(full_path):
                if directory in full_path and not os.path.isfile(full_path):
                    for filename in os.listdir(full_path):
                        check_file = os.path.join(full_path, filename)
                        if os.path.isfile(check_file):
                            condition_function(check_file)







