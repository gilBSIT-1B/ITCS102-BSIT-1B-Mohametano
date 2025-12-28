import os
from menu_def_file import num1, num2, num3, num4, num5, num6, num7, num8, num9
while True:
    print("Welcome to my")
    print("==================================")
    print("SIMPLE PROGRAM FOR TEACHING PYTHON")
    print("==================================")
    print("")

    x = input("Type (next) Here to Start ---> ").lower()
    if x == "next":
        while True:
            os.system("cls")
            print("Our Topics:")
            print("[1] - Python introduction")
            print("[2] - What is Variable and Print Output")
            print("[3] - Data Types")
            print("[4] - Input Function")
            print("[5] - Types of Operators")
            print("[6] - Conditional statements")
            print("[7] - Loop statement")
            print("[8] - List and Dictionary")
            print("[9] - Function and Input")
            print("[x] - Exit program")

            choice = input("""To start the program type the CODE the code is the one inside this "[]": """)

            if choice == "1":#intro
                os.system("cls")
                print("==================="
                    "PYTHON INTRODUCTION"
                    "===================\n\n"

                    "\"Python is a programming language that lets you work quickly and integrate systems more effectively.\"\n"
                    "\t- Guido van Rossum, creator of Python\n\n"

                    "Python is a high-level programming language that is simple to read,\n"
                    "easy to write, and powerful to use.\n\n"

                    "It was created to help people focus on solving problems\n"
                    "rather than dealing with complicated syntax.\n\n"

                    "Python is easy to learn but powerful enough for professionals.\n"
                    "Beginners can start with simple programs,\n"
                    "while experts use Python for large and complex systems.\n\n"

                    "=== WHY PYTHON? ===\n\n"

                    "Python is one of the best programming languages for beginners because:\n\n"
                    "\t• It uses simple English-like words\n"
                    "\t• It has fewer symbols and shorter code\n"
                    "\t• It is easy to read and understand\n"
                    "\t• It helps you learn programming logic faster\n\n"

                    "=== WHERE DO WE USE PYTHON? ===\n\n"

                    "Python is used in many real-world applications such as:\n\n"
                    "\t• Web development\n"
                    "\t• Game development\n"
                    "\t• Mobile and desktop applications\n"
                    "\t• Data analysis and data science\n"
                    "\t• Artificial Intelligence and Machine Learning\n"
                    "\t• Automation and scripting\n"
                    "\t• Cybersecurity tools\n\n"

                    "Many popular companies like Google, Netflix,\n"
                    "YouTube, and Instagram use Python.\n\n"

                    "\"Code is the language of the future.\"\n"
                    "Learning Python today prepares you for tomorrow.\n")
                exit = input("\n[X]Exit Python Introduction --> ").lower()
                if exit == "x":
                    os.system("cls")
                    print("Exited Python Introduction")
                    continue
            elif choice == "2":#print variable
                os.system("cls")
                print(
                "=== VARIABLES AND PRINT FUNCTION ===\n\n"
                "VARIABLES\n"
                "---------\n"
                "A variable is a container used to store information in a program.\n"
                "You give it a name, and you can store a value inside it such as a\n"
                "number, word, or sentence.\n\n"

                "#- Sa madaling salita, ang variable ay parang bag o lalagyan.\n"
                "Ito ang ginagamit para magtago ng value na pwede nating gamitin\n"
                "ulit-ulitin sa program.\n\n"

                "EXAMPLE:\n"
                "my_name = \"Gilcris\"\n"
                "age = 18\n\n"

                "Sa example na ito:\n"
                "\t• my_name at age ang variables\n"
                "\t• \"Gilcris\" at 18 ang kanilang values\n"
                "\t• Ang (=) ay tinatawag na assignment operator ito ay pang konekta sa variable at value\n\n"

                "============================================================\n\n"

                "CONGRATS! YOU ARE LEARNING THE BASICS OF PYTHON :)\n"
                )
                exit = input("\n[X]Exit Python Introduction --> ").lower()
                if exit == "x":
                    os.system("cls")
                    print("Exited VARIABLES AND PRINT FUNCTION")
                    continue


            elif choice == "3":# data types
                os.system("cls")
    
                print(
                    "=== DATA TYPES IN PROGRAMMING ===\n\n"

                    "Data types tell Python what kind of value a variable stores.\n"
                    "Select a data type to learn more:\n\n"

                    "\t[1] • String (str)\n"
                    "\t[2] • Integer (int)\n"
                    "\t[3] • Float (float)\n"
                    "\t[4] • Boolean (bool)\n\n"

                    "\t[X] • Exit\n"
                    )

                choice = input("Enter your choice: ")

                if choice == "1":
                        os.system("cls")
                        print(
                            "\n--- STRING (str) ---\n\n"
                            "A string is used to store text or characters.\n"
                            "It can include letters, symbols, and spaces.\n\n"
                            "#- Ginagamit ang string para sa text.\n\n"
                            "EXAMPLE:\n"
                            "name = \"Gilcris\"\n"
                            "message = \"Hello World!\"\n"
                        )
                        input("\nPress Enter to go back...")

                elif choice == "2":
                        os.system("cls")
                        print(
                            "\n--- INTEGER (int) ---\n\n"
                            "An integer is used to store whole numbers only.\n"
                            "Decimals are NOT allowed.\n\n"
                            "#- Ginagamit para sa buong numero.\n\n"
                            "EXAMPLE:\n"
                            "age = 18\n"
                            "year = 2025\n"
                        )
                        input("\nPress Enter to go back...")

                elif choice == "3":
                        os.system("cls")
                        print(
                            "\n--- FLOAT (float) ---\n\n"
                            "A float stores numbers with decimal points.\n"
                            "It represents real numbers.\n\n"
                            "#- Ginagamit para sa decimal numbers.\n\n"
                            "EXAMPLE:\n"
                            "price = 19.99\n"
                            "gpa = 3.1\n"
                        )
                        input("\nPress Enter to go back...")

                elif choice == "4":
                        os.system("cls")
                        print(
                            "\n--- BOOLEAN (bool) ---\n\n"
                            "A boolean represents truth values.\n"
                            "It can only be True or False.\n\n"
                            "#- Ginagamit kapag YES or NO lang ang sagot.\n\n"
                            "EXAMPLE:\n"
                            "is_active = True\n"
                            "is_dead = False\n"
                        )
                        input("\nPress Enter to go back...")

                elif choice == "x":
                        print("\nExiting Data Types lesson...")
                        break

                else:
                        print("\nInvalid choice. Please try again.\n")


            elif choice == "4":#input
                os.system("cls")
                print(
                "=== INPUT FUNCTION ===\n\n"

                "In Python, the input() function is used to get data from the user via the keyboard.\n"
                "When the program reaches an input() function, it pauses and waits for the user to type something\n"
                "and press Enter. The value entered by the user is then returned as a string.\n\n"

                "------------------------------------------------------------\n\n"

                "BASIC USAGE\n"
                "------------\n"
                "# Ginagamit natin ang input() para kumuha ng data mula sa user.\n"
                "Maaari rin nating i-assign ang input sa isang variable para ma-save ang data.\n\n"

                "EXAMPLE:\n"
                "x = input(\"Enter something: \")\n"
                "print(x)\n\n"

                "When we run this code, it will pause and wait for user input.\n"
                "If the user types Hello and presses Enter, the output will be:\n" \
                "Hello"
                "==========\n"
                )
                exit = input("\n[X]Exit Python Introduction").lower()
                if exit == "x":
                    os.system("cls")
                    print("Exited INPUT FUNCTION")
                    continue

            elif choice == "5":#operators
                os.system("cls")
                print(
                "=== TYPES OF OPERATORS ===\n\n"

                "Operators are symbols used to perform operations on values and variables.\n"
                "They allow Python to compute, compare, and make decisions.\n\n"

                "The most common operator types are:\n"
                "\t[1] • Arithmetic Operators\n"
                "\t[2] • Comparison Operators\n"
                "\t[3] • Logical Operators\n"
                "\t[4] • Assignment Operators\n\n"
                "\tENTER TO EXIT TYPE OF OPERATORS\n"
                        )
                choice = str(input("Choose where to start --> "))
                if choice == "1":
                    os.system("cls")
                    print(
                    "============================================================\n\n"

                    "1. ARITHMETIC OPERATORS\n"
                    "----------------------\n"
                    "Arithmetic operators are used to perform mathematical calculations.\n\n"

                    "SYMBOL | NAME                | WHAT IT DOES\n"
                    "-------|---------------------|----------------------------------------\n"
                    "+      | Addition            | Adds two values\n"
                    "-      | Subtraction         | Subtracts one value from another\n"
                    "*      | Multiplication      | Multiplies values\n"
                    "/      | Division            | Divides and returns a decimal result\n"
                    "%      | Modulus             | Returns the remainder of division\n"
                    "**     | Exponentiation      | Raises a number to a power\n"
                    "//     | Floor Division      | Divides and rounds down the result\n\n"

                    "#- Ginagamit ang arithmetic operators para sa math operations.\n\n"

                    "EXAMPLE:\n"
                    "a = 10\n"
                    "b = 3\n"
                    "print(a + b)   # 13\n"
                    "print(a %\ b)   # 1\n"
                    "print(a ** b)  # 1000\n\n"

                    "USING ARITHMETIC OPERATORS WITH range():\n"
                    "for i in range(1, 10 + 1):\n"
                    "\tprint(i)\n\n"
                    "#- Ginamit ang + operator para isama ang 10 sa loop.\n\n"

                    "============================================================\n\n"
                    )
                    input("\nPress Enter to go back...")
                elif choice == "2":
                    os.system("cls")
                    print(
                    "2. COMPARISON OPERATORS\n"
                    "----------------------\n"
                    "Comparison operators are used to compare two values.\n"
                    "They always return True or False.\n\n"

                    "SYMBOL | NAME                | WHAT IT DOES\n"
                    "-------|---------------------|----------------------------------------\n"
                    "==     | Equal to            | Checks if values are equal\n"
                    "!=     | Not equal to        | Checks if values are not equal\n"
                    ">      | Greater than        | Checks if left is greater\n"
                    "<      | Less than           | Checks if left is smaller\n"
                    ">=     | Greater or equal    | Checks if greater or equal\n"
                    "<=     | Less or equal       | Checks if less or equal\n\n"

                    "#- Ginagamit ito sa conditions at decision making.\n\n"

                    "EXAMPLE:\n"
                    "age = 18\n"
                    "print(age >= 18)  # True\n\n"

                    "============================================================\n\n"
                    )
                    input("\nPress Enter to go back...")

                elif choice == "3":
                    os.system("cls")
                    print(
                    "3. LOGICAL OPERATORS\n"
                    "-------------------\n"
                    "Logical operators are used to combine multiple conditions.\n\n"

                    "KEYWORD | NAME | WHAT IT DOES\n"
                    "--------|------|--------------------------------------------\n"
                    "and     | AND  | True if both conditions are True\n"
                    "or      | OR   | True if at least one condition is True\n"
                    "not     | NOT  | Reverses the result (True becomes False)\n\n"

                    "#- Ginagamit kapag may higit sa isang kondisyon.\n\n"

                    "EXAMPLE:\n"
                    "age = 20\n"
                    "has_id = True\n"
                    "print(age >= 18 and has_id)\n\n"

                    "============================================================\n\n"
                    )
                    input("\nPress Enter to go back...")

                elif choice == "4":
                    os.system("cls")
                    print(
                    "4. ASSIGNMENT OPERATORS\n"
                    "----------------------\n"
                    "Assignment operators are used to assign values to variables.\n\n"

                    "SYMBOL | NAME                | WHAT IT DOES\n"
                    "-------|---------------------|----------------------------------------\n"
                    "=      | Assign              | Assigns a value\n"
                    "+=     | Add and assign      | Adds then assigns\n"
                    "-=     | Subtract and assign | Subtracts then assigns\n"
                    "*=     | Multiply and assign | Multiplies then assigns\n"
                    "/=     | Divide and assign   | Divides then assigns\n\n"

                    "EXAMPLE:\n"
                    "x = 5\n"
                    "x += 3\n"
                    "print(x)  # 8\n\n"

                    "============================================================\n\n"

                    "SUMMARY\n"
                    "-------\n"
                    "- Operators help Python perform calculations and decisions.\n"
                    "- Arithmetic operators are often used with range() in loops.\n"
                    "- Comparison and logical operators are important for if-statements.\n\n"

                    "CONGRATS!\n"
                    "You just learned the Types of Operators in Python.\n"
                    "You're building a strong foundation as a programmer!\n"
                    )
                    input("\nPress Enter to go back...")
                elif choice == "x".lower:
                    print("EXIT TYPES OF OPERATORS")
                    break


            elif choice == "6":#CONDITIONAL
                print(
                "=== CONDITIONAL STATEMENTS IN PYTHON ===\n\n"

                "Conditional statements allow your program to make decisions based on conditions.\n"
                "They control which parts of your code run depending on whether a condition is True or False.\n\n"

                "------------------------------------------------------------\n\n"

                "BASIC STRUCTURE\n"
                "---------------\n"
                "# Python uses if, elif, and else keywords for conditional statements.\n\n"

                "1. if statement - runs a block of code if the condition is True.\n"
                "2. elif statement - checks another condition if the previous 'if' was False.\n"
                "3. else statement - runs a block of code if all previous conditions are False.\n\n"

                "EXAMPLE 1: Simple Number Check\n"
                "--------------------------------\n"
                "number = int(input('Enter a number: '))\n"
                "if number > 0:\n"
                "\tprint('Positive number')\n"
                "elif number == 0:\n"
                "\tprint('Zero')\n"
                "else:\n"
                "\tprint('Negative number')\n\n"

                "Try entering a number and see what the program prints!\n\n"

                "EXAMPLE 2: Grading System\n"
                "-------------------------\n"
                "score = int(input('Enter your score: '))\n"
                "if score >= 90:\n"
                "\tprint('Excellent')\n"
                "elif score >= 75:\n"
                "\tprint('Good')\n"
                "else:\n"
                "\tprint('Needs Improvement')\n\n"

                "Now you can enter your own score and see your grade!\n\n"

                "LEZGAWWWWWW!\n"
                "You have learned how to use conditional statements in Python.\n"
                )
                
                exit = input("\n[X]Exit CONDITIONAL STATEMENTS --> ")
                if exit == "x":
                    os.system("cls")
                    print("Exited CONDITIONAL STATEMENTS")
                    continue
                else:
                    print("INVALID INPUT")


            elif choice == "7":#LOOOP
                    print(
                        "=== LOOP STATEMENTS IN PYTHON ===\n\n"
                        "Loop statements allow your program to repeat a block of code multiple times.\n"
                        "You can choose which type of loop to learn:\n\n"
                        "\t[1] For Loop\n"
                        "\t[2] While Loop\n"
                        "\t[3] Back / Exit\n"
                    )

                    pili = input("Enter your choice (1/2/3): ")
                    if pili == "1":
                        print(
                            "\n=== FOR LOOP IN PYTHON ===\n\n"

                            "A for loop is used to iterate over a sequence, such as a list, string, or numbers.\n"
                            "The range() function is often used to generate numbers for iteration.\n\n"

                            "Example with range:\n"
                            "for i in range(1, 10, 2):\n"
                            "\tprint(i)\n\n"

                            "# Explanation:\n"
                            "# 1 - start: the number where counting begins (inclusive)\n"
                            "# 10 - stop: the number where counting stops (exclusive)\n"
                            "# 2 - step: how much to increase after each iteration\n\n"

                            "# So this loop will print:1-10 pababa\n"
                            "# It starts at 1, stops before 10, and increases by 2 each time.\n\n"

                            "You can also use range with only one number:\n"
                            "for i in range(5):\n"
                            "\tprint(i)\n"
                            "# This will print 0, 1, 2, 3, 4\n"
                            "# Default start is 0 and step is 1.\n\n"
                        )
                        input("\nPress Enter to go back...")
                        
                        

                    elif pili == "2":
                        os.system("cls")
                        print(
                            "\n=== WHILE LOOP IN PYTHON ===\n\n"

                            "A while loop runs a block of code as long as a condition is True.\n"
                            "Be careful to avoid infinite loops!\n\n"

                            "Example:\n"
                            "count = 0\n"
                            "while count < 5:\n"
                            "\tprint('Count is', count)\n"
                            "\tcount += 1\n\n"
                            "# This will print numbers 0 to 4.\n\n"

                            "You can also use input inside a while loop:\n"
                            "user_input = ''\n"
                            "while user_input != 'quit':\n"
                            "\tuser_input = input('Type something (or quit to stop): ')\n"
                            "\tprint('You typed:', user_input)\n\n"

                            "Try typing different words to see how the loop works!\n"
                        )
                        exit = input("\n[X]Exit While Loop").lower()
                        if exit == "x":
                            os.system("cls")
                            print("Exited While Loop")
                            break
                        

                    elif choice == "3":
                        print("Returning to the main menu...\n")
                        break
                    else:
                        print("Invalid choice. Please select 1, 2, or 3.\n")

            elif choice == "8":#List and dictionary
                print(
                "=== LISTS AND DICTIONARIES IN PYTHON ===\n\n"
                "In this lesson, you can choose which topic to learn first:\n\n"
                "\t[1] Lists\n"
                "\t[2] Dictionaries\n"
                "\t[3] Back / Exit\n"
                )

                choice = input("Enter your choice (1/2/3): ")
                if choice == "1":
                    print(
                        "\n=== LISTS IN PYTHON ===\n\n"

                        "A list is an ordered collection of items that can be changed.\n"
                        "Lists can store different types of data, like numbers, strings, or even other lists.\n\n"

                        "Creating a list:\n"
                        "fruits = ['apple', 'banana', 'cherry']\n"
                        "print(fruits)  # Output: ['apple', 'banana', 'cherry']\n\n"

                        "Accessing elements:\n"
                        "print(fruits[0])  # prints 'apple'\n"
                        "print(fruits[-1]) # prints 'cherry'\n\n"

                        "Modifying a list:\n"
                        "fruits[1] = 'orange'\n"
                        "print(fruits)  # Output: ['apple', 'orange', 'cherry']\n\n"

                        "Adding items:\n"
                        "fruits.append('kiwi')\n"
                        "print(fruits)\n\n"

                        "Removing items:\n"
                        "fruits.remove('apple')\n"
                        "print(fruits)\n\n"

                        "Lists are useful for storing multiple values and managing data efficiently.\n"
                    )
                    exit = input("\n[X]Exit LIST").lower()
                    if exit == "x":
                            os.system("cls")
                            print("Exited LIST")
                            break

                elif choice == "2":
                    print(
                        "\n=== DICTIONARIES IN PYTHON ===\n\n"

                        "A dictionary is a collection of key-value pairs.\n"
                        "Each key is unique and is used to access its value.\n\n"

                        "Creating a dictionary:\n"
                        "person = {'name': 'John', 'age': 25, 'city': 'Manila'}\n"
                        "print(person)  # Output: {'name': 'John', 'age': 25, 'city': 'Manila'}\n\n"

                        "Accessing values:\n"
                        "print(person['name'])  # prints 'John'\n"
                        "print(person.get('age')) # prints 25\n\n"

                        "Modifying values:\n"
                        "person['age'] = 26\n"
                        "print(person)  # Output: {'name': 'John', 'age': 26, 'city': 'Manila'}\n\n"

                        "Adding new key-value pairs:\n"
                        "person['job'] = 'Developer'\n"
                        "print(person)\n\n"

                        "Removing items:\n"
                        "del person['city']\n"
                        "print(person)\n\n"

                        "Dictionaries are very useful when you want to store related data and access it by keys.\n"
                    )
                    exit = input("\n[X]Exit Dictionary").lower()
                    if exit == "x":
                            os.system("cls")
                            print("Exited Dictionary")
                            break
                elif choice == "3":
                    print("Returning to the main menu...\n")
                    break
                else:
                    print("Invalid choice. Please select 1, 2, or 3.\n")
            elif choice == "9":#Function and input
                print(
                    "=== FUNCTIONS AND IMPORTS IN PYTHON ===\n\n"
                    "In this lesson, you can choose which topic to learn first:\n\n"
                    "\t[1] Functions\n"
                    "\t[2] Import Statement\n"
                    "\t[3] Back / Exit\n"
                )

                choice = input("Enter your choice (1/2/3): ")

                if choice == "1":
                    print(
                        "=== FUNCTIONS IN PYTHON ===\n\n"
                        "Functions are blocks of reusable code that perform a specific task.\n"
                        "They help make your programs organized and easier to read.\n\n"

                        "Example 1: Simple function\n"
                        "def greet():\n"
                        "\tprint('Hello! Welcome to Python Functions!')\n\n"
                        "# Calling the function:\n"
                        "greet()\n\n"

                        "Example 2: Function with parameters\n"
                        "def greet_person(name):\n"
                        """\tprint(f'Hello, \{name!}')\n\n"""
                        "# Call with a name:\n"
                        "greet_person('Alice')\n\n"

                        "Example 3: Function returning a value\n"
                        "def add_numbers(a, b):\n"
                        "\treturn a + b\n"
                        "result = add_numbers(5, 3)\n"
                        "print('The sum is', result)\n\n"

                        "Notice how functions organize code and can be reused multiple times.\n"
                    )
                    exit = input("\n[X]Exit Functions").lower()
                    if exit == "x":
                            os.system("cls")
                            print("Exited Functions")
                            break

                elif choice == "2":
                    print(
                        "=== IMPORT STATEMENT IN PYTHON ===\n\n"
                        "The import statement lets you use modules in your code.\n"
                        "Python has many built-in modules you can import, like 'math' and 'os'.\n\n"

                        "Example 1: Using the math module (built-in)\n"
                        "import math\n"
                        "print(math.sqrt(16))  # Output: 4.0\n\n"

                        "Example 2: Using the os module (built-in)\n"
                        "import os\n"
                        "print('Current directory:', os.getcwd())\n\n"

                        "You can also use your own functions with imports.\n"
                        "For example, if you have defined a function 'greet_person(name)' in another file:\n"
                        "# from my_functions import greet_person\n"
                        "greet_person('Alice')  # Output: Hello, Alice!\n\n"

                        "Notice how imports let your program use extra tools or your own functions,\n"
                        "making your code more powerful and organized.\n"
                    )
                    exit = input("\n[X]Exit Imort ").lower()
                    if exit == "x":
                            os.system("cls")
                            print("Exited function and import")
                            break

                elif choice == "3":
                    print("Returning to the main menu...\n")
                    break

                else:
                    print("Invalid choice. Please select 1, 2, or 3.\n")
            elif choice == "x":
                os.system("cls")
                print("EXIT PROGRAM")
                break
            else:
                os.system("cls")
                print("INPUT INCORRECT")
                continue
        else:
            print("Maybe you typed the word (NEXT) Incorrectly?")

            

            