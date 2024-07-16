from tkinter import *
import tkinter.messagebox as tmsg

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(scvalue.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

x_root = Tk()
x_root.title("Calculator Using Tkinter")
x_root.geometry("644x744")
x_root.wm_iconbitmap(".\\Data\\calculator_22175.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(x_root,textvariable=scvalue,font="lucide 40  bold")
screen.pack(fill=X,ipadx=10,padx=10)

count=-1
for i in range(3):
    f1=Frame(x_root,bg="Grey")
    count += 1
    b=Button(f1,text=f"{9-count}",font="lucida 25 bold",padx=25,pady=18)
    b.pack(side=LEFT,padx=18,pady=5)
    b.bind("<Button-1>",click)
    count += 1
    b=Button(f1,text=f"{9-count}",font="lucida 25 bold",padx=25,pady=18)
    b.pack(side=LEFT,padx=18,pady=5)
    b.bind("<Button-1>", click)
    count += 1
    b=Button(f1,text=f"{9-count}",font="lucida 25 bold",padx=25,pady=18)
    b.pack(side=LEFT,padx=18,pady=5)
    b.bind("<Button-1>", click)
    f1.pack()

f1=Frame(x_root,bg="Grey")
b=Button(f1,text="0",font="lucida 25 bold",padx=26,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="+",font="lucida 25 bold",padx=26,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>", click)
b=Button(f1,text="-",font="lucida 25 bold",padx=26,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>", click)
f1.pack()

f1=Frame(x_root,bg="Grey")
b=Button(f1,text="/",font="lucida 25 bold",padx=27,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="%",font="lucida 25 bold",padx=23,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>", click)
b=Button(f1,text="=",font="lucida 25 bold",padx=25,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>", click)
f1.pack()

f1=Frame(x_root,bg="Grey")
b=Button(f1,text="C",font="lucida 25 bold",padx=25,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text=".",font="lucida 25 bold",padx=25,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>", click)
b=Button(f1,text="00",font="lucida 25 bold",padx=25,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>", click)
f1.pack()

x_root.mainloop()