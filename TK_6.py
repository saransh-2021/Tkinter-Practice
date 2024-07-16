from tkinter import *

x_root = Tk()
x_root.geometry("655x333")

def hello():
    print("Hello tkinter buttons")
def name():
    print("name is saransh")
frame1=Frame(x_root,borderwidth=6,bg="grey",relief=SUNKEN)
frame1.pack(side=LEFT,anchor="nw")

b1= Button(frame1,fg="red", text="Print Now",command=hello)
b1.pack(side=LEFT,padx=23)
b2= Button(frame1,fg="red", text="Tell ME nAME Now",command=name)
b2.pack(side=LEFT,padx=23)
b3= Button(frame1,fg="red", text="Print Now")
b3.pack(side=LEFT,padx=23)
b4= Button(frame1,fg="red", text="Print Now")
b4.pack(side=LEFT,padx=23)

x_root.mainloop()