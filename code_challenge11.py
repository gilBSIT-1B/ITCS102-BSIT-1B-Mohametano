for x in range(0, 10, 1):
    for sangkalan in range(x,18 , 1):
        print(" ", end=" ")
    for rs in range(1, x+1, 1):
        print("*", end=" ")
    for rs in range(1, x, 1):
        print("*", end=" ")
    print()

for x in range(10, 0, -1):
    for sangkalan in range(18,x,-1):
        print(" ", end=" ")
    for rs in range(1, x+1, 1):
        print("*", end=" ")
    for rs in range(1, x, 1):
        print("*", end=" ")
    print()