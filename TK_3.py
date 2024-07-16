from tkinter import *
from PIL import Image, ImageTk

x_root = Tk()

# image size 494x468
x_root.geometry("550x510")
#x_root.maxsize(550,510)
#x_root.minsize(550,510 )

#for png images
photo = PhotoImage(file=".\\Data\\5ede4a3fb760540004f2c5e9 for tk_3.png")
Label(text="hello").pack()
photo_label = Label(image=photo)
photo_label.pack()

#dor jpg images
image = Image.open(".\\Data\\512c9a9bfd71ae7ab6b583dca74c318f for tk_3.jpg")
image1 = ImageTk.PhotoImage(image)
image1_label = Label(image=image1)
image1_label.pack()

x_root.mainloop()