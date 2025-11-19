import os
import json
os.system('cls')
print("==========================")
print("STUDENT INFORMATION SYSTEM")
print("==========================")

student_record = {}

while True: 
    print("SELECT FROM THE FOLLOWING OPTIONS")
    print("A - Add student record")
    print('B - Print all student record')
    print('C - Search Student Record')
    print('D - Delete Student Record0')
    print('E - Edit Student Record')
    print("F - Export Student Record")
    print("G - Exit System")

    choice = input('SELECT FROM THE OPTIONS ABOVE ---> ').lower()
    os.system('cls')

    if choice == 'a':
        print("Adding student record")
        id_no = (input("Please input ID number ---> "))
        first_name = input('Please input first name ---> ').upper()
        last_name = input('Please input Last Name ---> ').upper()
        age=eval(input("Please input age ---> "))
        course=input('Please input Course --->').upper()
        section=input("Please input section ---> ").upper()
        student_record[id_no]=[first_name,last_name,age,course,section]
        print("================================================\t")
        print("STUDENT INFORMATION HAS BEEN SAVED SUCCESSFULLY.\t")
        print("================================================")
        pass
        continue

    elif choice == 'b':
        os.system('cls')
        print('PRINTING STUDENT RECORD')
        print(student_record)
        for i, j in student_record.items(): #key - value
            print(f"STUDENT ID - {i}, INFORMATION - {j}")
        pass
        continue
    elif choice == 'c':
        os.system('cls')
        print("SEARCH STUDENT RECORD")
        search_id = input("Input Student ID for search --->").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print('===================')
                print(f'\n\nRECORD FOUND for ID {search_id}')#para hanapin id 
                for i in student_record[search_id]:
                    print(f'--- {i}')
                print('===================')
                
                
                print('RECORD FOUND')
            else:
                print("RECORD NOT FOUND")
            break
        continue

    elif choice == 'd':
        print("DELETE STUDENT RECORD")
        search_id = input("Input Student ID for search").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print('===================')
                print(f'\n\nRECORD FOUND for ID {search_id}')#para hanapin id 
                for i in student_record[search_id]:
                    print(f'--- {i}')
                print('===================')
                student_record.pop(search_id)
                
                print('\nRECORD DELETED')
            else:
                print("RECORD NOT FOUND")
            break
        pass
        continue
    elif choice == 'e':
        os.system('cls')
        print("SEARCH STUDENT RECORD")
        search_id = input("Input Student ID to DELETE --->").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print('===================')
                print(f'\n\nRECORD FOUND for ID {search_id}')#para hanapin id 
                for i in student_record[search_id]:
                    print(f'--- {i}')
                print('===================')
                print("Editing student record")
                first_name = input('Please input first name ---> ').upper()
                last_name = input('Please input Last Name ---> ').upper()
                age=eval(input("Please input age ---> "))
                course=input('Please input Course --->').upper()
                section=input("Please input section ---> ").upper()
                student_record[id_no]=[first_name,last_name,age,course,section]
                os.system('cls')
                print('RECORD SUCCESSFULLY EDITED')
            
            else:
                print("RECORD NOT FOUND")
                break
    elif choice == 'f':
        print("EXPORT STUDENT DATA")
        #JSON JAVASCRIPT OBJECT NOTATION
        with open('student_record.json','w') as new_file:
            json.dump(student_record,new_file,indent=4 )
        pass
    elif choice == 'g':
        os.system('cls')
        print("YOU HAVE EXITED THE SYSTEM")
        break
    else:
        print("Invalid Input")
