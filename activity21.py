isdirty = True
sum = 0
while isdirty == True:
    confirm = input("Do you want to continue washing ( yes / no ): ").lower()
    sum += 1
    if confirm == 'yes':
        print("Washing Washing continues...")
        continue
    else:
        print("Washing Washing stops...")
        break

print("The number of cycle is", sum)