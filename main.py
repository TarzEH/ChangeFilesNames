import os
from tkinter import *
from  gui_file import *





#GUI

run()


#Functions
def condition_function(filename):
    if os.path.isfile(filename):
        check_file_new = filename.replace(" ", "")
        os.rename(filename, check_file_new)
        filename = check_file_new
        check_file_new = filename.replace("@", "")
        os.rename(filename, check_file_new)
        filename = check_file_new
        check_file_new = filename.replace("!", "")
        os.rename(filename, check_file_new)
        filename = check_file_new
        check_file_new = filename.replace("#", "")
        os.rename(filename, check_file_new)
        filename = check_file_new
        check_file_new = filename.replace("%", "")
        os.rename(filename, check_file_new)
        filename = check_file_new
        check_file_new = filename.replace("$", "")
        os.rename(filename, check_file_new)
        filename = check_file_new
        return;





#Program
os.chdir(os.path.join(os.getenv('HOME'), 'Desktop'))
directory = input("insert Directory Name:")
path=os.walk(os.getcwd())
for root, directories, files in path:
        for path in os.listdir(root):
            full_path = os.path.join(root, path)
            #if os.path.isfile(full_path):
            if directory in full_path and not os.path.isfile(full_path):
                for filename in os.listdir(full_path):
                    check_file = os.path.join(full_path, filename)
                    if os.path.isfile(check_file):
                        condition_function(check_file)







