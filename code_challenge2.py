amount = eval(input("Type your deposit here -->"))

print("Here is your deposit")
print("1000 -",amount // 1000)
amount = amount % 1000
print("500 -",amount // 500)
amount = amount % 500
print("200 -",amount // 200)
amount = amount % 200
print("100 -",amount // 100)
amount = amount % 100
print("50 -",amount // 50)
amount = amount % 50
print("20 -",amount // 20)
amount = amount % 20
print("10 -",amount // 10)
amount = amount % 10
print("5 -",amount // 5)
amount = amount % 5
print("1 -",amount // 1)