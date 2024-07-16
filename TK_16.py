from tkinter import *
import tkinter.messagebox as tmsg

def order():
    tmsg.showinfo("order received", f"we hve received your order of {var.get()}")

x_root = Tk()
x_root.title("RadioButtons In Tkinter")
x_root.geometry("644x344")

var = IntVar()
#var.set(1)
Label(x_root,text="ap kya kahyenge?",justify=LEFT,padx=14).pack()

radio = Radiobutton(x_root,text="dosa",padx=14,variable=var,value=1).pack(anchor="w")
Radiobutton(x_root,text="idli",padx=14,variable=var,value=2).pack(anchor="w")
Radiobutton(x_root,text="parantha",padx=14,variable=var,value=3).pack(anchor="w")
Radiobutton(x_root,text="samosa",padx=14,variable=var,value=4).pack(anchor="w")

Button(text="order niw",command=order).pack()
x_root.mainloop()