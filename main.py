import os
from tkinter import *
from functools import partial


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
def run(directory,env):
    os.chdir(os.path.join(os.getenv(directory), env))
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






if __name__ == "__main__":
    #GUI
    root = Tk()

    root.title("Change files name app")
    root.configure(width=500, height=300)
    root.configure(bg='lightgray')
    label1 = Label(root, padx=50, pady=20, text="Hi, insert Directory Name: ")
    label1.pack()
    import_user = Entry(root)
    import_user.pack()
    label2 = Label(root, padx=70, pady=20, text="insert Env Name: ")
    label2.pack()
    import_user2 = Entry(root)
    import_user2.pack()
    MyButton = Button(root, pady=10, padx=50, text="submit", command=lambda: run(import_user.get(),import_user2.get()))
    MyButton.pack()


    root.mainloop()










