from tkinter import *
window = Tk()
window.config(bg="sky blue")
window.title("Profile Builder")
#commmands
def change ():
    window.config(bg="Pink")
    
def change1 ():
    window.config(bg="sky blue")

def StudentID():
    NEW = Toplevel()
    NEW.title("StudentID")
    NEW.config(bg="Sky Blue")
    label2 = Label(NEW, text="Profile Builder",font=("Arial",20,"bold"),bg="sky blue")
    label2.grid(column=0,row=0, columnspan=2,)

    named = Label(NEW, text="Name:",bg="sky blue",pady=5)
    named.grid(row=1, column=0)

    ages = Label(NEW, text="Age:",bg="sky blue",pady=5)
    ages.grid(row=2, column=0)

    named = Label(NEW, text="Gender:",bg="sky blue",pady=5)
    named.grid(row=3, column=0)

    namet = Label(NEW, text=u_firstname.get(),bg="sky blue",pady=5)
    namet.grid(row=1, column=2)
    

label = Label(window, text="Profile Builder",font=("Arial",20,"bold"),bg="sky blue")
label.grid(column=0,row=0, columnspan=4,)

frame = Frame(window,bg="red")
frame.grid(column=1, row=1, columnspan=4, rowspan=5)

#--------Entry boxes-----
u_firstname = Entry(window)
u_firstname.grid(row=1, column=1, padx=5)

u_middlename = Entry(window)
u_middlename.grid(row=1, column=2,padx=5)

u_lastname = Entry(window)
u_lastname.grid(row=1, column=3, padx=5)


#--------Buttons---------

b_firstname = Label(window, text="First Name",bg="sky blue")
b_firstname.grid(row=2, column=1,padx=5)

b_middlename = Label(window, text="Middle Name",bg="sky blue")
b_middlename.grid(row=2, column=2,padx=5)

b_lastname = Label(window, text="Last Name",bg="sky blue")
b_lastname.grid(row=2, column=3,padx=5)

#--------second entry
u_birthyear = Entry(window)
u_birthyear.grid(row=3, column=1, padx=5)

#--------second entry
b_lastname = Label(window, text="Birth Year",bg="sky blue")
b_lastname.grid(row=4, column=1,padx=5)

#--------gender
ugender = Label(window, text="Gender",bg="sky blue")
ugender.grid(row=5, column=1,padx=5)

gender = StringVar(value="Male")



rb_male = Radiobutton(window, text="Male", variable=gender, value="Male",bg="Sky Blue", command=change1)
rb_male.grid(row=5, column=2, padx=5)

rb_female = Radiobutton(window, text="Female", variable=gender, value="Female",bg="Sky Blue", command=change)
rb_female.grid(row=5, column=3, padx=5)

submit = Button(window, text="Submit", command=StudentID)
submit.grid(row=6, column=0, columnspan=4,pady=5)




window.mainloop()