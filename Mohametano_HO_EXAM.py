from tkinter import *

from matplotlib import use
window = Tk()
window.title("EXAM")
window.configure(bg="Black")

usern = ""

def register():
    Register_window = Toplevel()
    Register_window.title("REGISTER")
    def Login_naba():
        label.config(text="Buy premium to unlock", width=20)
    label = Label(Register_window, text="Registration Form", font=("compact", 25, "bold"), fg="Black", bg="White",width=15)
    label.grid(row=0, column=0, columnspan=2)

    label1 = Label(Register_window, text="Username", font=("compact", 15, "bold"),width=15)
    label1.grid(row=1, column=0)

    usern = Entry(Register_window)
    usern.grid(row=1, column=1)


    label2 = Label(Register_window, text="Username", font=("compact", 15, "bold"),width=15)
    label2.grid(row=2, column=0)

    passw = Entry(Register_window)
    passw.grid(row=2, column=1)

    show = Checkbutton(Register_window, text="Show Password")
    show.grid(row=3,column=0,columnspan=2)

    Done = Button(Register_window, text="Register", bg="black", fg="White", command=Login_naba)
    Done.grid(row=4, column=0, columnspan=2)

    

def login():
    login_window = Toplevel()
    login_window.title("Log_in")
    login_window.configure(bg="Green")

    def passwordcheck():
        Log_label.config(text="Buy premium to unlock", width=20)
    good = Label(login_window, text="HElloi") 
    good.grid(row=0, column=0, columnspan=2)

    Log_label = Label(login_window, text="Log In",font=("compact", 25, "bold"), fg="Black", bg="Green",width=15 )
    Log_label.grid(row=0, column=0, columnspan=2)

    Log_label1 = Label(login_window, text="Username", font=("compact", 15, "bold"),width=15, bg="green",padx=5)
    Log_label1.grid(row=1, column=0)

    pas = Label(login_window, text="Password", font=("compact", 15, "bold"),width=15, bg="green",padx=5)
    pas.grid(row=2, column=0)

    Log_label_entry = Entry(login_window)
    Log_label_entry.grid(row=1, column=1)

    pass_label_entry = Entry(login_window, show="*")
    pass_label_entry.grid(row=2, column=1)

    show1 = Checkbutton(login_window, text="Show Password", bg="Green")
    show1.grid(row=3,column=0,columnspan=2)

    Done1 = Button(login_window, text="Log In",font=("compact", 10, "bold"), fg="Black", bg="Green", width=35, command=passwordcheck)
    Done1.grid(row=4, column=0, columnspan=2)


user_form = Label(window, text="Welcome", font=("compact", 40, "bold"), fg="White", bg="Black",width=15)
user_form.pack()

Register = Button(text="Register",font=("compact", 30, "bold"), fg="White", bg="Gray",width=20,command=register)
Register.pack()

Log_in = Button(text="Log_in",font=("compact", 30, "bold"), fg="White", bg="Gray",width=20, command=login)
Log_in.pack(padx=5,pady=5)




window.mainloop()