from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    x_root.title("Untitled-Notpad")
    file=None
    textArea.delete(1.0,END)

def openFile():
    global file
    file=asksaveasfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        x_root.title(os.path.basename(file)+"- Notepad")
        textArea.delete(1.0,END)
        f=open(file,"r")
        textArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file =  asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(textArea.get(1.0,END))
            f.close()

            x_root.title(os.path.basename(file)+"- Notepad")
            print("file saved")
    else:
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()

def cut():
    textArea.event_generate("<<Cut>>")

def copy():
    textArea.event_generate("<<Copy>>")

def paste():
    textArea.event_generate("<<Paste>>")

def about():
    tmsg.showinfo("Notepad","Notepad by Saransh on tkinter")

if __name__ == '__main__':

    x_root = Tk()
    x_root.title("Creating a GUI Notepad In Tkinter")
    x_root.geometry("644x588")
    x_root.wm_iconbitmap(".\\Data\\notepad_bloc_notes_15549.ico")

    #add text area
    textArea=Text(x_root,font="lucida 13")
    file=None
    textArea.pack(fill=BOTH,expand=TRUE)

    #lets create a menu bar
    MenuBar=Menu(x_root)
    #file menu starts
    fileMenu=Menu(MenuBar,tearoff=0)
    #to open new file
    fileMenu.add_command(label="New",command=newFile)
    #open existing file
    fileMenu.add_command(label="Open",command=openFile)
    #save current file
    fileMenu.add_command(label="Save",command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="exit",command=x_root.destroy)
    MenuBar.add_cascade(label="File",menu=fileMenu)
    #file menu ends

    # file edit starts
    EditMenu = Menu(MenuBar, tearoff=0)
    # to give a feature of cut, copy,paste
    EditMenu.add_command(label="cut",command=cut)
    EditMenu.add_command(label="copy", command=copy)
    EditMenu.add_command(label="paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    # edit menu ends

    # help menu starts
    helpMenu = Menu(MenuBar, tearoff=0)
    helpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=helpMenu)
    # help menu ends
    x_root.config(menu=MenuBar)

    #adding scrollbar
    scroll=Scrollbar(textArea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=textArea.yview)
    textArea.config(yscrollcommand=scroll.set)


    x_root.mainloop()