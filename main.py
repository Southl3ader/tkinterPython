from tkinter import *


def read_info():
    file = open("user.txt","r")
    i = 0
    var = []
    while True :
        st = file.readline()
        var.insert(i,st)
        i+=1
        if st == "":
            break
    file.close()
    return var


def show():
    listView.delete(0, END)
    listuser = read_info()
    o1 = 1
    for o in range(0, len(listuser)):
        listView.insert(o1, listuser.__getitem__(o))
        o1 += 1

def serach_user():
    userView.delete(0, END)
    for i in range(0,len(listuser)):
        j = listuser[i]
        g = j.split()
        if studentidsearch.get() == g[2]:
            userView.insert(1,g[0]+"   "+g[1]+"   "+g[2]+"   "+g[3])
            break

def remove_user():
    listuser= read_info()
    for i in range(0,len(listuser)):
        j = listuser[i]
        g = j.split()
        print(len(listuser))
        if studentidsearch.get() == g[2]:
            listuser.remove(listuser[i])
            break
    save_list(listuser)

def  save_list(listuser):
    file = open("user.txt", "w")
    q = len(listuser)-1
    for i in range(0,q):
        j = listuser[i]
        g = j.split()
        file.write(g[0])
        file.write("    ")
        file.write(g[1])
        file.write("    ")
        file.write(g[2])
        file.write("    ")
        file.write(g[3])
        file.write("\n")
    file.close()
    show()

def save_info():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    studentid_info = studentid.get()
    age_info = age.get()
    age_info = str(age_info)
    print(firstname_info, lastname_info, studentid_info, age_info)

    file = open("user.txt", "a")
    file.write(firstname_info)
    file.write("    ")
    file.write(lastname_info)
    file.write("    ")
    file.write(studentid_info)
    file.write("    ")
    file.write(age_info)
    file.write("\n")
    file.close()
    print(" User ", firstname_info, " has been registered successfully")

    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    studentid_entry.delete(0, END)
    age_entry.delete(0, END)
    show()


screen = Tk()
screen.geometry("800x600",)
screen.title("Moshakhasate Daneshjo")
heading = Label(text="Moshakhasate Daneshjo", bg="skyBlue", fg="black", width="500", height="3")
heading.pack()

listView = Listbox(width=40,)
listuser = read_info()
o1 = 1
for o in range(0, len(listuser)):
    listView.insert(o1, listuser.__getitem__(o))
    o1 += 1
listView.place(x=300, y=90)

userView = Listbox(width=40,height=1)
userView.place(x=15, y=450)

firstname_text = Label(text="Firstname : ",)
lastname_text = Label(text="Lastname : ", )
studentid_text = Label(text="Student ID : ", )
age_text = Label(text="Age : ", )
searchl = Label(text="Search :",)
searchStudent = Label(text="Enter student ID : ",)
firstname_text.place(x=15, y=70)
lastname_text.place(x=15, y=120)
studentid_text.place(x=15, y=170)
age_text.place(x=15, y=220)
searchl.place(x=15, y=380)
searchStudent.place(x=15, y=400)

firstname = StringVar()
lastname = StringVar()
studentid = StringVar()
age = IntVar()
studentidsearch = StringVar()

firstname_entry = Entry(textvariable=firstname, width="30")
lastname_entry = Entry(textvariable=lastname, width="30")
studentid_entry = Entry(textvariable=studentid, width="30")
age_entry = Entry(textvariable=age, width="30")
studentid_entry_search = Entry(textvariable=studentidsearch, width="30")
firstname_entry.place(x=15, y=90)
lastname_entry.place(x=15, y=140)
studentid_entry.place(x=15, y=190)
age_entry.place(x=15, y=240)
studentid_entry_search.place(x=15, y=420)

register = Button(screen, text="Register", width="25", height="2", command=save_info, bg="skyBlue")
register.place(x=15, y=290)
remove = Button(screen, text="Remove", width="25",height="2",command=remove_user, bg="skyBlue")
remove.place(x=300, y=500)
serach = Button(screen, text="Search", width="25",height="2",command=serach_user, bg="skyBlue")
serach.place(x=15, y=500)
update = Button(screen, text="Update", width="25",height="2", bg="skyBlue")
update.place(x=500, y=500)
screen.mainloop()