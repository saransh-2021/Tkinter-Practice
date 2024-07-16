from tkinter import *

x_root = Tk()
x_root.title("More Tkinter Tips, Tricks & Functions")
x_root.geometry("644x344")

#
x_root.wm_iconbitmap(".\\Data\\death_halloween_23228.ico")
x_root.configure(background="grey")
width = x_root.winfo_screenwidth()
height = x_root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="Close", command=x_root.destroy).pack()

x_root.mainloop()