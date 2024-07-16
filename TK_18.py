from tkinter import *

x_root = Tk()
x_root.title("ScrollBar In Tkinter")
x_root.geometry("644x344")

# For connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command=widget.yview)

scrollbar= Scrollbar(x_root)
scrollbar.pack(side=RIGHT,fill=Y)
lbx=Listbox(x_root,yscrollcommand=scrollbar.set)
for i in range(343):
    lbx.insert(END,f"Item {i}")
lbx.pack(fill=BOTH,pady=22)
#text = Text(x_root, yscrollcommand = scrollbar.set)
#text.pack(fill=BOTH)
scrollbar.config(command=listbox.yview)
#scrollbar.config(command=text.yview)

x_root.mainloop()