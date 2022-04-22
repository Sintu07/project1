from tkinter import *
from tkinter import ttk
from turtle import width
from tkinter import messagebox

#global declare


# ************************************************student dashboard**************************************************************
def win1():
    win = Tk()
    win.geometry("900x700")
    # function call************************

    def add():
        firstn =e1.get()
        s = e1.get()
        print("hello")
        print(s)
        print(firstn)
#***********************************************



    # main-frame
    frm = Frame(win, bg="#DC143C")
    frm.place(x=0, y=0, width=900, height=100)

    # main frame title
    l = Label(frm, text="School Management System",
              font=("", 20, "bold"), bg="#DC143C", bd=2)
    l.pack()

    # frame 2
    frm2 = Frame(win, bg="#B0C4DE", relief=FLAT)
    frm2.place(x=0, y=100, width=700, height=400)
    
    
    
    
    # frame 3
    frm3 = Frame(frm2, bg="BLACK")
    frm3.place(x=0, y=0, width=700, height=50)
    l1 = Label(frm3, text="Manage Student", font=(
        "", 20, "bold"), bg="black", fg="white", bd=2)
    l1.pack()




    # # tables
    # # table 1
    fname = Label(frm2, text="First Name:", font=(
        "times new roman", 22, "bold"), bg="black", fg="white")
    fname.place(x=0, y=60)
    e1 = Entry(frm2, font=(
        "times new roman", 12, "bold"), relief=RIDGE)
    e1.place(x=0, y=100)

    #   # table 2
    lname = Label(frm2, text="last Name:", font=(
        "times new roman", 20, "bold"), bg="black", fg="white")
    lname.place(x=200, y=60)
    e2 = Entry(frm2, font=(
        "times new roman", 12, "bold"), relief=RIDGE)
    e2.place(x=200, y=100)

    #   # table 3
    css = Label(frm2, text="class:", font=(
        "times new roman", 20, "bold"), bg="black", fg="white")
    css.place(x=400, y=60)
    i = ['first year', 'second', 'third', 'four']
    css_combo = ttk.Combobox(frm2, values=i)
    css_combo.place(x=400, y=100, width=140, height=30)
    css_combo.config(state="readonly")
    css_combo.set("select")

    # # table 4
    iname = Label(frm2, text="ID NO:", font=(
        "times new roman", 22, "bold"), bg="black", fg="white")
    iname.place(x=0, y=150)
    e3 = Entry(frm2, font=(
        "times new roman", 12, "bold"), relief=RIDGE)
    e3.place(x=0, y=200)
    #   # table 5
    emal = Label(frm2, text="Email :", font=(
        "times new roman", 20, "bold"), bg="black", fg="white")
    emal.place(x=200, y=150)
    e4 = Entry(frm2, font=(
        "times new roman", 12, "bold"), relief=RIDGE)
    e4.place(x=200, y=200)
    #  # table 6
    con = Label(frm2, text="Contact No.:", font=(
        "times new roman", 20, "bold"), bg="black", fg="white")
    con.place(x=400, y=150)
    e5 = Entry(frm2, font=(
        "times new roman", 12, "bold"), relief=RIDGE)
    e5.place(x=400, y=200)

    # #    # table 7
    dob = Label(frm2, text="D_O_B", font=(
        "times new roman", 20, "bold"), bg="black", fg="white")
    dob.place(x=0, y=250)
    e1 = Entry(frm2, font=(
        "times new roman", 12, "bold"), relief=RIDGE)
    e1.place(x=0, y=300)
    # #  # table 6
    addr = Label(frm2, text="Address:", font=(
        "times new roman", 22, "bold"), bg="black", fg="white")
    addr.place(x=200, y=250)
    e6 = Entry(frm2, font=(
        "times new roman", 12, "bold"), relief=RIDGE)
    e6.place(x=200, y=300, width=170, height=50)
    # #   # table 7
    g1 = Label(frm2, text="Gender", font=(
        "times new roman", 22, "bold"), bg="black", fg="white")
    g1.place(x=400, y=250)
    i = ['male', 'female']
    g1_combo = ttk.Combobox(frm2, values=i)
    g1_combo.place(x=400, y=300, width=140, height=30)
    g1_combo.config(state="readonly")
    g1_combo.set("MALE")

    # fuction

    # #BUTTON
    B1 = Button(self.frm2, text="Add", width=6, font=(
        "times new roman", 15, "bold"), bg="black", fg="#7FFFD4", command=add)
    B1.place(x=600, y=100)


# ************************************************ main window function cALLL*******************************************************************

def main():
    win = Tk()
    win.geometry("700x500")
    win.resizable(width=False, height=False)
    win.config(bg="#ff9d4d")

    def mainf():
        user = e1.get()
        passw = e2.get()
        if user == "" and passw == "":
            messagebox.showerror("error", "Enter user id and password")

        elif user == "sintu" and passw == "704246":
            win1()

        else:
            messagebox.showerror(
                "WRONG PASSWORD", "Enter VALID user id and password ")

    #global declare

    # frmae declare

    frm = Frame(win)

    frm.configure(bg="#a6a6a6")
    frm.place(x=100, y=50, width=500, height=400)
# label
    Label(frm, text=("Login"), width=14, font=(
        "", 22, "bold"), bg="#ffcccc").pack()
# login code label
    user = Label(frm, text="User ID", width=10, font=("Bold", 22, "bold"))
    user.place(x=10, y=100)
# Entery user
    e1 = Entry(frm, bd=4)
    e1.place(x=300, y=100, width=120, height=40)

# login password label
    user = Label(frm, text="Password", width=10, font=("black", 22, "bold"))
    user.place(x=10, y=200)
    # password enetry
    e2 = Entry(frm,show='*', bd=4)
    e2.place(x=300, y=200, width=120, height=40)


# login into window BUTTON1
    login = Button(frm, text=("Login"), width=14, font=(
        "", 22, "bold"), bg="#a6a6a6", command=mainf)
    login.place(x=60, y=300, width=120, height=30)

# forget lab BUTTON2
    login = Button(frm, text=("NEW USER"), width=28,
                   font=("", 18, "bold"), bg="#a6a6a6")
    login.place(x=200, y=300, width=160, height=30)
    win.mainloop()


main()
