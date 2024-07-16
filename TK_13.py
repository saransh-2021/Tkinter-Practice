from tkinter import *

def myfunc():
    print("HELLO")
x_root = Tk()
x_root.title("Menus & Submenus in Tkinter")
x_root.geometry("644x344")

'''#use these to creat a non dopdown menu
mymenu = Menu(x_root)
mymenu.add_command(label="File",command=myfunc)
mymenu.add_command(label="Exit",command=quit)
x_root.config(menu=mymenu)'''

#use this fro a dropdown menu
mainmenu = Menu(x_root)

m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="new",command=myfunc)
m1.add_command(label="save",command=myfunc)
m1.add_separator()
m1.add_command(label="save as",command=myfunc)
m1.add_command(label="print",command=myfunc)
#x_root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="cut",command=myfunc)
m2.add_command(label="copy",command=myfunc)
m2.add_separator()
m2.add_command(label="paste",command=myfunc)
m2.add_command(label="find",command=myfunc)
#x_root.config(menu=mainmenu)
mainmenu.add_cascade(label="edit",menu=m2)

x_root.config(menu=mainmenu)

x_root.mainloop()