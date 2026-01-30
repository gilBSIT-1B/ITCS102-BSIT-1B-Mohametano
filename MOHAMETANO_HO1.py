inp = input("type ka ng word bossing: ")
inpn = len(inp)
n = 0
print(f"Ang nilagay mo boss na word ay may {inpn} na letters")
for i in range (1,inpn+1):
    num = int(input(f"type ka ng number bossing {i}: "))
    n += num
print(f"Ang total ng tinype mong numbers ay: {n}")
ave = n / inpn
print(f"Ang average ng tinype mong numbers ay: {ave}")