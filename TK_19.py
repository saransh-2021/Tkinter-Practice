from tkinter import *
import time

def upload():
    statusvar.set("Busy..")
    sbar.update()
    time.sleep(2)
    statusvar.set("Ready Now")

x_root = Tk()
x_root.title("Status Bar In Tkinter")
x_root.geometry("644x344")

statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(x_root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(x_root,text="Upload",command=upload).pack()

x_root.mainloop()