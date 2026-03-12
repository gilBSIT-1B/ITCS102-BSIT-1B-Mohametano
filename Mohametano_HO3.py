from tkinter import *
window = Tk()
window.title("GRID")
window.config(bg="lightblue")

def add():
    f1 = fnum.get()
    s1 = snum.get()
    answer = float(f1) + float(s1)
    sagot.config(text=f"The sum of {f1} and {s1} ")
    sagot.grid(row=0, column=0, columnspan=4)
    answer12.config(text=f"is {answer}")
    answer12.grid(row=1, column=0, columnspan=4)

def subtract():
    f1 = fnum.get()
    s1 = snum.get()
    answer = float(f1) - float(s1)
    sagot.config(text=f"The difference of {f1} and {s1} is {answer}")
    sagot.grid(row=0, column=0, columnspan=4)

def multiply():
    f1 = fnum.get()
    s1 = snum.get()
    answer = float(f1) * float(s1)
    sagot.config(text=f"The product of {f1} and {s1} is {answer}")
    sagot.grid(row=0, column=0, columnspan=4)

def divide():
    f1 = fnum.get()
    s1 = snum.get()
    answer = float(f1) / float(s1) if float(s1) != 0 else "Error"
    sagot.config(text=f"The quotient of {f1} and {s1} is {answer}")
    sagot.grid(row=0, column=0, columnspan=4)

answer12 = Label(window, text="", font=("compact", 25, "bold"),bg="lightblue", fg="black")
answer12.grid(row=1, column=0, columnspan=4)
sagot = Label(window, text="MY SIMPLE CALCULATOR", font=("compact", 25, "bold"),bg="lightblue", fg="black")
sagot.grid(row=0, column=0, columnspan=4)

u_label = Label(window, text="Enter 1st Number:", width=20, font=("compact", 10, "bold"))
u_label.grid(row=2, column=1, padx=10, pady=10)

plabel = Label(window, text="Enter 2nd Number:", width=20, font=("compact", 10, "bold"))
plabel.grid(row=3, column=1, padx=10, pady=10)


fnum = Entry(window, width=30,
                bg="lightgray", fg="black", borderwidth=2,font=("compact", 10, "bold"))
fnum.grid(row=2, column=2, padx=10, pady=10)

snum = Entry(window, width=30,
                bg="lightgray", fg="black", borderwidth=2,font=("compact", 10, "bold"))
snum.grid(row=3, column=2, padx=10, pady=10)

add_but = Button(window, text="Add", font=("compact", 10, "bold"), bg="white", fg="black", command=add, activebackground="red")
add_but.grid(row=4, column=1, pady=10)

add_but2 = Button(window, text="Subtract", font=("compact", 10, "bold"), bg="white", fg="black", command=subtract, activebackground="orange")
add_but2.grid(row=4, column=2, pady=10)

add_but3 = Button(window, text="Multiply", font=("compact", 10, "bold"), bg="white", fg="black", command=multiply, activebackground="lightgreen")
add_but3.grid(row=5, column=1, pady=10)

add_but4 = Button(window, text="Divide", font=("compact", 10, "bold"), bg="white", fg="black", command=divide, activebackground="lightpink")
add_but4.grid(row=5, column=2, pady=10)


window.mainloop()