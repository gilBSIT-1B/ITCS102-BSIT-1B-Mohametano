isdirty = True
sum = 0
while isdirty == True:
    confirm = input("Do you want to continue washing ( yes / no ): ").lower()
    if confirm == 'yes':
        print("Washing Washing continues...")
        sum += 1
        continue
    elif confirm== 'no':
        print("Washing Washing stops...")
        break
    else:
        print("yes or no?")

print("The number of cycle is", sum)
mo = 0
import random
guessed = True
while guessed == True:
    guess = random.randint(1,10)
    x = int(input(f"Guess the Random number (1,10): "))
    mo += 1
    if x == guess:
        print("Congratulations you've guessed it right!!!")
        break
        
    else:
        print("ENGKKKK!!, Guess again")
        continue
print(f"You've guessed right in your {mo}'th try.")