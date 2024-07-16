from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0
x_root = Tk()
x_root.title("ListBox In Tkinter")
x_root.geometry("644x344")

lbx = Listbox(x_root)
lbx.pack()
lbx.insert(END,"dirst tim of lbx")
Button(x_root,text="add item",command=add).pack()

x_root.mainloop()