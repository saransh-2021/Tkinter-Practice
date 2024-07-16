from tkinter import *

x_root = Tk()
x_root.geometry("655x333")
f1=Frame(x_root,bg="green",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y,pady=60)
f2 = Frame(x_root,borderwidth=8,bg="red",relief=SUNKEN)
f2.pack(side=TOP,fill=X)

l1=Label(f1,text="Project tk - pycharm")
l1.pack(pady=142)
l1=Label(f2,text="welcome to sublime text",font="helvetica 20 italic")
l1.pack()
x_root.mainloop()