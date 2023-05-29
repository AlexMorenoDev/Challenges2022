# Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).

def is_amstrong_number(n):
    if n < 0:
        return False

    s_n = str(n)

    sum = 0
    for e in s_n:
        sum += int(e) ** 3

    return sum == n

print(is_amstrong_number(371)) # True
print(is_amstrong_number(-371)) # False
print(is_amstrong_number(372)) # False
print(is_amstrong_number(0)) # True
print(is_amstrong_number(1)) # True