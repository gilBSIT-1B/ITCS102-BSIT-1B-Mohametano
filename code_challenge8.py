print("Multiplication table MAKER!!")
x = eval(input("Enter a number: "))
print("\nMultiplication table for",x,":")
for xyz in range(1,11):
    xy = x * xyz
    print(x,"x",xyz,"=",xy)