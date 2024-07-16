from tkinter import *

#root is window now
#and in class root is self
class GUI(Tk):
    def __init__(self):
            super().__init__()
            self.geometry("344x377")

    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self,textvariable=self.var,relief=SUNKEN,anchor="w")
        self.statusbar.pack(side=BOTTOM,fill=X)

    def click(self):
        print("Button Click")

    def createbutton(self,intext):
        Button(text=intext,command=self.click).pack()

if __name__ == '__main__':
    window=GUI()
    window.status()
    window.createbutton("click me+")
    window.mainloop()
