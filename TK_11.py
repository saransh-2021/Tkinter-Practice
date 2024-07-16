from tkinter import *

def harry(event):
    print(f"You  click button at {event.x},{event.y}")
x_root = Tk()
x_root.title("Events in Tkinter")
x_root.geometry("644x344")

widget = Button(x_root,text="Click me please")
widget.pack()

widget.bind('<Button-1>',harry)
widget.bind('<Double-1>',quit)

x_root.mainloop()