# Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.

def recursive_factorial(n):
    if n < 0:
        return "No factorial"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
    

# Non recursive function
def factorial(n):
    if n < 0 :
        return "No factorial"

    result = 1
    for i in range(1, n+1):
        result *= i

    return result

print(recursive_factorial(7))
print(factorial(7))