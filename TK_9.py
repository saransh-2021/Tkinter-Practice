from tkinter import *

x_root = Tk()
x_root.geometry("644x344")

def getvals():
    print("Submitting Form")

    print(f"{name_value.get(),phone_value.get(),gender_value.get(),emergency_value.get(),paymentmode_value.get(),foodservice_value.get()}")

    with open("Records.txt","a") as f:
        f.write(f"{name_value.get(),phone_value.get(),gender_value.get(),emergency_value.get(),paymentmode_value.get(),foodservice_value.get()}\n")
        f.flush()

#heading
Label(x_root,text="Welcome to Harry Travels",pady=15).grid(row=0,column=3)

#text for forms
name = Label(x_root,text="Name")
phone = Label(x_root,text="Phone")
gender = Label(x_root,text="Gender")
emergency = Label(x_root,text="Emergency Contact")
paymentmode = Label(x_root,text="Payment Mode")

#pack text with grid
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

#tkinter vars for storing data
name_value = StringVar()
phone_value = StringVar()
gender_value = StringVar()
emergency_value = StringVar()
paymentmode_value = StringVar()
foodservice_value = IntVar()

#entries for forms
nameentry = Entry(x_root,textvariable=name_value)
phoneentry = Entry(x_root,textvariable=phone_value)
genderentry = Entry(x_root,textvariable=gender_value)
emergencyentry = Entry(x_root,textvariable=emergency_value)
paymentmodeentry = Entry(x_root,textvariable=paymentmode_value)

#packing the entries forms
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

#checkbox and packing
foodservice = Checkbutton(text="Want TO prebook your meals",variable=foodservice_value)
foodservice.grid(row=6,column=3)

#button and packing and assigning it
Button(text="Submit to harry travels",command=getvals).grid(column=3,row=7,pady=5)

x_root.mainloop()