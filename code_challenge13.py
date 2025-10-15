name = input("What's your name?: ")
sum = 0
odd=""
print("+++++++++++++++++++++++++++++++++++++ \nODD NUMBER SUMMATION, press 0 to stop\n+++++++++++++++++++++++++++++++++++++")
num = True
while num == True:
    x = eval(input("Input a random number: "))
    if x %2 == 1:
        sum += x
        odd += str(x)
        continue
    elif x == 0:
        print("Program stops")
        break
print(f"Hi {name} the sum of all number is {sum}")
print("ODD numbers detected included the following", odd)
    
    
