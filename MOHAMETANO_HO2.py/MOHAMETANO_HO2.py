import tkinter as tk
window = tk.Tk()

window.title("MOHAMETANO_HO2")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg="gray")

label = tk.Label(window, text="STUDENT PROFILE", font=("Arial", 24, "bold"), bg="gray",fg="black")
label.pack(pady=20)

label = tk.Label(window, text="Full Name: Gilcris R. Mohametano", font=("Arial", 24), bg="gray",fg="white")
label.pack(pady=20, padx=20,anchor="w")

label = tk.Label(window, text="Age: 18years old", font=("Arial", 24), bg="gray",fg="white", justify= "left")
label.pack(pady=20, padx=20,anchor="w")

label = tk.Label(window, text="Course: BSIT", font=("Arial", 24), bg="gray",fg="white", justify= "left")
label.pack(pady=20, padx=20, anchor="w")

label = tk.Label(window, text="Birthday: October 02, 2007", font=("Arial", 24), bg="gray",fg="white", justify= "left")
label.pack(pady=20,padx=20, anchor="w")

label = tk.Label(window, text="Motto:", font=("Arial", 24), bg="gray",fg="white", justify= "left")
label.pack(pady=20, padx=20, anchor="w")

label = tk.Label(window, text=f"         If you can think it, you can do it!🫂", font=("Arial", 24), bg="gray",fg="red", justify= "left")
label.pack(pady=20, padx=20, anchor="w")


label = tk.Label(window, text=f"""
                 Twinkle, twinkle, little star, 
                 how I wonder what you are. 
                 Up above the world so high,
                 like a diamond in the sky. 
                 Twinkle, twinkle, little star,
                 how I wonder what you are.
                 When the blazing sun is set, 
                 and the grass with dew is wet.
                 Then you show your little
                 light, twinkle, twinkle all the night. 
                 Twinkle, twinkle little star, 
                 how I wonder what you are.
""", font=("Arial", 24), bg="gray",fg="red", justify= "left")
label.pack(anchor="center")
window.mainloop()