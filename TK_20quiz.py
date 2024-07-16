from tkinter import *

class GUI(Tk):
    def __init__(self,width,height):
        super().__init__()
        self.geometry(f"{width}x{height}")

    def clickbutton(self):
        import time
        self.statusbar.set("Saving")
        self.sbar.update()
        time.sleep(2)
        self.statusbar.set("Ready")

    def createbutton(self,bname):
        Button(self,text=bname,anchor="sw",command = self.clickbutton).pack(side="bottom")

    def textarea(self):
        self.scrollbar = Scrollbar(self)
        self.text = Text(self,yscrollcommand=self.scrollbar.set,width=80)
        self.text.pack(side="left")
        self.scrollbar.config(command =self.text.yview)
        self.scrollbar.pack(side="left",fill=Y)

    def status(self):
        self.statusbar = StringVar()
        self.statusbar.set("Ready")
        self.sbar = Label(self,textvariable=self.statusbar,anchor="sw")
        self.sbar.pack(side="bottom",fill=X)


if __name__ == "__main__":
    window = GUI(665,600)
    window.status()
    window.createbutton("Save")
    window.textarea()
    window.mainloop()