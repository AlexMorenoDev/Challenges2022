# Enunciado: Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
# - Utiliza el menor número de líneas para resolver el ejercicio.

# num_years -> number of years to print
# current -> initial leap year, function will start printing from that year
def print_next_leap_years(num_years, current):
    for _ in range(1, num_years+1):
        current += 4
        print(current)


print_next_leap_years(30, 2020)