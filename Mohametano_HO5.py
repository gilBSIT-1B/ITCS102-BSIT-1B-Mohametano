import os

your_dreams = "dreams.txt"

def create_file(): # creating a sample
    if not os.path.exists(your_dreams):
        f = open(your_dreams, "w")
        f.write("Dream Big: I want to become a skilled programmer who builds systems that help people.\n" \
        "Stay Curious: I will keep learning even when things get difficult.\n"
        "Embrace Failure: Every error is a step closer to success.\n"
        "Create Impact: I want my code to solve real-world problems.\n"
        "Be Consistent: Small progress every day leads to big results.\n"
        "Believe in Yourself: I am capable of learning and growing. Someday we will be free")

        f.close()
        print("File 'dreams.txt' created successfully!")

def read_messages():# 1
    print("\n--- YOUR INSPIRING MESSAGES ---")
    f = open(your_dreams, "r")
    content = f.read()
    f.close()
    
    if content == "":
        print("The file is empty.")
    else:
        print(content)
    print("-------------------------------")


def add_message():# 2
    print("\n--- ADD NEW MESSAGE ---")
    new_message = input("Enter your message: ")
    
    if new_message != "":
        f = open(your_dreams, "a")  
        f.write("new_message")
        f.close()
        print("Message has been added!")
    else:
        print("You entered nothing.")

def rewrite_file(): #3
    print("\n--- REWRITE FILE ---")
    DELETE = input("This deletes everything. Type 'yes' to continue: ")
    
    if DELETE.lower() == "yes":
        print("Type your new text below. Type 'DONE' when finished:")
        
        all_lines = []
        while True:
            line = input().lower()
            if line == "done":
                break
            all_lines.append(line)
            
        final_text = "\n".join(all_lines)
        
        f = open(your_dreams, "w") 
        f.write(final_text + "\n")
        f.close()
        print("File rewritten!")
    else:
        print("Cancelled.")

create_file() #MAIN MENU
while True:
    print("\n==========================")
    print("   DREAMS MANAGER MENU")
    print("==========================")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")
    print("==========================")
    
    choice = input("Choose 1-4: ")
    
    print("\n" * 2) 

    if choice == "1":
        os.system('cls')
        read_messages()
    elif choice == "2":
        os.system('cls')
        add_message()
    elif choice == "3":
        os.system('cls')
        rewrite_file()
    elif choice == "4":
        os.system('cls')
        print("Thankyou for using my program")
        break
    else:
        print("Choose a Number from 1-4")