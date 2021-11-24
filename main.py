from tkinter import *


def save_info():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    studentid_info = studentid.get()
    age_info = age.get()
    age_info = str(age_info)
    print(firstname_info, lastname_info, studentid_info, age_info)

    file = open("user.txt", "a")
    file.write(firstname_info)
    file.write("*")
    file.write(lastname_info)
    file.write("*")
    file.write(studentid_info)
    file.write("*")
    file.write(age_info)
    file.write("\n")
    file.close()
    print(" User ", firstname_info, " has been registered successfully")

    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    studentid_entry.delete(0,END)
    age_entry.delete(0, END)


screen = Tk()
screen.geometry("500x500")
screen.title("Moshakhasate Daneshjo")
heading = Label(text="Python Form", bg="grey", fg="black", width="500", height="3")
heading.pack()

firstname_text = Label(text="Firstname * ", )
lastname_text = Label(text="Lastname * ", )
studentid_text = Label(text="Student ID *", )
age_text = Label(text="Age * ", )
firstname_text.place(x=15, y=70)
lastname_text.place(x=15, y=120)
studentid_text.place(x=15, y=170)
age_text.place(x=15, y=220)

firstname = StringVar()
lastname = StringVar()
studentid = StringVar()
age = IntVar()

firstname_entry = Entry(textvariable=firstname, width="30")
lastname_entry = Entry(textvariable=lastname, width="30")
studentid_entry = Entry(textvariable=studentid, width="30")
age_entry = Entry(textvariable=age, width="30")
firstname_entry.place(x=15, y=90)
lastname_entry.place(x=15, y=140)
studentid_entry.place(x=15, y=190)
age_entry.place(x=15, y=240)

register = Button(screen, text="Register", width="30", height="2", command=save_info, bg="grey")
register.place(x=15, y=290)
screen.mainloop()