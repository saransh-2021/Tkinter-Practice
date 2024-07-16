from tkinter import *
import tkinter.messagebox as tmsg

def myfunc():
    print("HELLO")

def help():
    print("i will help you")
    tmsg.showinfo("help","i will help you in this gui")

def rateus():
    print("rate us")
    value=tmsg.askquestion("was your xp","wyou used thi sgui")
    if value == "yes":
        msg= "rate us on ncu"
    else:
        msg="what was worng?"
    tmsg.showinfo("experiecen",msg)

def divya():
    ans=tmsg.askretrycancel("divya se dosti kr lo","sorry divya slut hai")
    if ans:
        print("retry krne se kuch nhi hota")
    else:
        print("gand maar uski")

x_root = Tk()
x_root.title("Message Box in Tkinter")
x_root.geometry("644x344")

mainmenu = Menu(x_root)

m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="new",command=myfunc)
m1.add_command(label="save",command=myfunc)
m1.add_separator()
m1.add_command(label="save as",command=myfunc)
m1.add_command(label="print",command=myfunc)
mainmenu.add_cascade(label="File",menu=m1)

m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="cut",command=myfunc)
m2.add_command(label="copy",command=myfunc)
m2.add_separator()
m2.add_command(label="paste",command=myfunc)
m2.add_command(label="find",command=myfunc)
mainmenu.add_cascade(label="edit",menu=m2)

m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label="help",command=help)
m3.add_command(label="rate",command=rateus)
m3.add_command(label="befriend_divya",command=divya)
mainmenu.add_cascade(label="help",menu=m3)

x_root.config(menu=mainmenu)

x_root.mainloop()