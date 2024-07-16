from tkinter import *
import tkinter.messagebox as tmsg

def getdollar():
    print(f"you got {myslider2.get()} dollars")
    tmsg.showinfo("Congratulations",f"you got {myslider2.get()} dollars")

x_root = Tk()
x_root.title("Sliders In Tkinter Using Scale()")
x_root.geometry("644x344")

#VERTICAL Slider
#myslider = Scale(x_root,from_=0,to=100)
#myslider.pack()
Label(x_root,text="how many dollars you want?").pack()
myslider2 = Scale(x_root,from_=0, to=100, orient=HORIZONTAL,tickinterval=50)
myslider2.pack()
myslider2.set(30)
Button(x_root,text="Get dollars", pady=10, command=getdollar).pack()
x_root.mainloop()