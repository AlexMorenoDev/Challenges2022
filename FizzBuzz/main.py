# Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), 
# sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "Fizz".
# - Múltiplos de 5 por la palabra "Buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) 