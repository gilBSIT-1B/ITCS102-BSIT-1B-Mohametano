import openpyxl
from datetime import datetime

def favperson():
    year_now = datetime.now().year
    data = []

    print("--- Favorite People Recorder ---")
    print("Please enter information for 3 favorite person.\n")

    for x in range(1, 4):
        print(f"Person {x}:")

        fname = input("First Name: ").strip()
        lname = input("Last Name: ").strip()

        while True:
            try:
                byear = int(input("Birth Year: ").strip())

                if byear < 1900 or byear > year_now:
                    print(f"Please enter a valid birth year between 1900 and {year_now}.")
                else:
                    break

            except ValueError:
                print("Invalid input. Please enter a numeric year.")

        age = year_now - byear

        data.append([
            x,
            fname,
            lname,
            byear,
            age
        ])
        print()

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Favorite People"

    head = ["ID", "First Name", "Last Name", "Birth Year", "Age"]
    ws.append(head)

    for row in data:
        ws.append(row)

    file = "favorite_people.xlsx"
    wb.save(file)

    print(f"Data successfully saved to '{file}'.\n")

    print("=== Records ===")
    print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Birth Year':<12} {'Age':<5}")
    print("-" * 55)

    for row in data:
        print(f"{row[0]:<5} {row[1]:<15} {row[2]:<15} {row[3]:<12} {row[4]:<5}")

favperson()