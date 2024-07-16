from tkinter import *
import pandas as pd
import numpy as np
import xlsxwriter
import tkinter.messagebox as tmsg

def Submit():
    #to get and write the data in the dataframe and create columns if not present
    name_value = name.get()
    age_value = age.get()
    contact_value = contact.get()
    mail_value = mail.get()
    xp_value = xp.get()
    data1.loc[len(data1.index)]={'Name': name_value, 'Age': age_value, 'Contact': contact_value, 'Mail': mail_value, 'Experience': xp_value}
    tmsg.showinfo("Data added",f"{name.get()} value inserted to Database")

'''
def Close():
    data1.to_excel(".\\Data\\TK_7quiz data.xlsx", sheet_name="Sheet1", columns=['Name', 'Age', 'Contact', 'Mail' , 'Experience'])
    root.destroy()
'''

'''
data1["Blank_Column"] = " "
data1["NaN_Column"] = np.nan
data1["None_Column"] = None
'''

try:
    #to check whether the file exists or not
    #if not then create it in the except clause
    #if exists then open it
    data1 = pd.read_excel(".\\Data\\TK_7quiz data.xlsx")
except:
    #if file does not exists then create and open it
    workbook = xlsxwriter.Workbook('.\\Data\\TK_7quiz data.xlsx')
    workbook.close()
    data1 = pd.read_excel(".\\Data\\TK_7quiz data.xlsx")

if data1.columns.empty:
    #to create columns if no columns are present in excel database
    # Use either None or "" for other than integer
    data1.insert(0, "Name", "")
    data1.insert(1, "Age", np.nan)
    data1.insert(2, "Contact", None)
    data1.insert(3, "Mail", None)
    data1.insert(4, "Experience", None)
    #        OR
    #data1["Name"] = ""
    #data1["Age"] = np.nan
    #data1["Contact"] = None
    #data1["Mail"] = None
    #data1["Experience"] = None

root = Tk()

root.geometry("355x250")
root.minsize(355, 250)
root.maxsize(355, 250)

root.title("Helvetica Dance Academy")
Label(root, text="Dance Academy Form", font="Calibri 15 bold", borderwidth=5, anchor="n").grid(column=0, columnspan=2)

name = StringVar()
Label(root, text="Enter Your Name").grid()
Entry(root, textvariable=name).grid(row=1, column=1)

age = IntVar()
Label(root, text="Enter Your Age").grid()
Entry(root, textvariable=age).grid(row=2, column=1)

contact = StringVar()
Label(root, text="Enter Your Contact No.").grid()
Entry(root, textvariable=contact).grid(row=3, column=1)

mail = StringVar()
Label(root, text="Enter Your Mail").grid()
Entry(root, textvariable=mail).grid(row=4, column=1)

xp = BooleanVar()
Label(root, text="Enter Your Experience (0=No/1=Yes)").grid(padx=10)
Entry(root, textvariable=xp).grid(row=5, column=1)

Button(root, text="Submit", command=Submit, height=2, width=10, relief=RIDGE, borderwidth=3).grid(column=1, pady=7)
Button(root, text="Exit", command=root.destroy, height=2, width=10, relief=RIDGE, borderwidth=3).grid(pady=5)

root.mainloop()
#to write the dataframe to the excel file
data1.to_excel(".\\Data\\TK_7quiz data.xlsx", sheet_name="Sheet1", columns=['Name', 'Age', 'Contact', 'Mail' , 'Experience'])