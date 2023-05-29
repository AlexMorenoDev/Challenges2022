# Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
# - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

def get_greatest(n1, n2):
    if n1 > n2:
        return n1, n2
    return n2, n1

# Euclidean Algorithm
def gcd(n1, n2):
    greatest, lowest = get_greatest(n1, n2)
    remainder = None
    while True:
        remainder = greatest % lowest
        if remainder == 0:
            break
        
        greatest = lowest
        lowest = remainder
        
    return lowest

# Formula: (n1 * n2)/GCD(n1, n2)
def lcm(n1, n2):
    return int((n1*n2)/gcd(n1, n2))

print(gcd(56, 180)) # 4
print(lcm(24, 60)) # 120



