def calculate_factorial(number, data_type):
    result = 1

    for i in range(1, number + 1):
        result *= i

        
        if data_type == "char" and result > 127:
            print("Faktoriāla vērtība pārsniedz char datu tipa robežas.")
            break
        elif data_type == "int" and result > 2147483647:
            print("Faktoriāla vērtība pārsniedz int datu tipa robežas.")
            break
        elif data_type == "long long" and result > 9223372036854775807:
            print("Faktoriāla vērtība pārsniedz long long datu tipa robežas.")
            break

    return result


number = int(input("Ievadiet decimālo skaitli: "))
data_type = input("Izvēlieties datu tipu (char, int vai long long): ")


result = calculate_factorial(number, data_type)
print(f"{number}! =", result)
