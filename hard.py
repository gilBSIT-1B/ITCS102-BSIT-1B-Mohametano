utang = eval(input("Magkano ang uutangin mo?: "))
tagal = eval(input("Ilang taon mo babayaran? "))

months = tagal * 12
babayaran = utang / months
babayaran_pa = utang
print("\tMonths\t\t|\tPrincipal Payment\t|\tRemaining Balance\t|\tInterest\t")

for i in range(1, months+1):
    babayaran_pa -= babayaran
    interest = babayaran_pa*.03
    monthly_payent = babayaran + interest
    print(f"{i}\t{round(babayaran,2)}\t\t|\t{round(interest,2)}\t\t\t|\t{round(babayaran_pa,2)}\t\t\t|\t 3%")