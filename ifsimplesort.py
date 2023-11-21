number1 = int(input("Ievadiet pirmo decimālo skaitli: "))
number2 = int(input("Ievadiet otro decimālo skaitli: "))
number3 = int(input("Ievadiet trešo decimālo skaitli: "))

kartošanas_seciba = input("Izvēlieties kārtošanas secību (augoša/dilstoša): ").lower()

if kartošanas_seciba == "augoša":
    sorted_numbers = sorted([number1, number2, number3])
elif kartošanas_seciba == "dilstoša":
    sorted_numbers = sorted([number1, number2, number3], reverse=True)
else:
    print("Nederīga kārtošanas secības izvēle. Lūdzu, ievadiet 'augoša' vai 'dilstoša'.")
    exit()

print("Sakārtotā secība:", sorted_numbers)
