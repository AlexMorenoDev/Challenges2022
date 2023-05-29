# Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.

# https://matematicasies.com/Averiguar-si-un-numero-es-primo
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        if n / i < i:
            return True

    return True

for i in range(2, 101):
    if isPrime(i):
        print(i)
