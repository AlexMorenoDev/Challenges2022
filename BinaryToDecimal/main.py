# Enunciado: Crea un programa se encargue de transformar un número binario a decimal sin utilizar
# funciones propias del lenguaje que lo hagan directamente.

def binary_to_decimal(binary):
    result = 0
    i = len(binary) - 1
    for n in binary:
        if n == "1":
            result += 2**i
        i -= 1

    return result 

# Faster method
def binary_to_decimal_2(binary):
    result = 0
    for n in binary:
        result = (result * 2) + int(n) 
    
    return result

print(binary_to_decimal("10011011")) # 155
print(binary_to_decimal("1000111111011110000101010101")) # 150856021

print(binary_to_decimal_2("10011011")) # 155
print(binary_to_decimal_2("1000111111011110000101010101")) # 150856021