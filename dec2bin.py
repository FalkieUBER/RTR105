skaitlis = int(input("Ievadiet naturālu skaitli: "))

bin_kods = bin(skaitlis)[2:]
print("Ievadītā skaitļa binārais kods:", bin_kods)

skaitlis1 = skaitlis << 1
skaitlis2 = skaitlis >> 1  


print("Bitu maiņa (<<):", skaitlis1)
print("Bitu maiņa (>>):", skaitlis2)
