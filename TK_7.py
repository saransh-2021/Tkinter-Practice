from tkinter import *
from tkinter.ttk import *

def getvals():
    print(avalue.get())
    print(bvalue.get())

x_root = Tk()
x_root.geometry("655x333")

#
a= Label(x_root,text="Username")
b= Label(x_root,text="Password")
a.grid()
b.grid(row=1)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

avalue = StringVar()
bvalue = StringVar()

aentry = Entry(x_root,textvariable=avalue)
bentry = Entry(x_root,textvariable=bvalue)

aentry.grid(row=0, column=1)
bentry.grid(row=1,column=1)

Button(text="Submit", command=getvals).grid()

x_root.mainloop()
