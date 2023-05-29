# Enunciado: Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno). 
# ¿De cuántas maneras eres capaz de hacerlo? Crea el código para cada una de ellas.

def iteration_1():
    for i in range(1, 101):
        print(i)

def iteration_2():
    i = 1
    while i <= 100:
        print(i)
        i += 1

def iteration_3():
    i = 1
    while True:
        print(i)
        i += 1
        if i > 100:
            break

# Recursive
def iteration_4(n):
    if n > 0:
        iteration_4(n-1)
        print(n)

def iteration_5():
    for num in list(range(1, 101)):
        print(num)