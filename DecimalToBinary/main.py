# Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

def reverse_string(string):
    r_string = ""

    i = len(string) - 1
    while i >= 0:
        r_string += string[i]
        i -= 1
    
    return r_string

def decimal_to_binary(n):
    remainders = ""
    while n > 0:
        remainders += str(n % 2)
        n = int(n / 2)
    
    remainders += "b0"
    binary = reverse_string(remainders)
    return binary

print(decimal_to_binary(200))