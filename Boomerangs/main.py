"""
 * Enunciado: Crea una función que retorne el número total de bumeranes de un array de números
 * enteros e imprima cada uno de ellos.
 * - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números seguidos, en el que el
 *   primero y el último son iguales, y el segundo es diferente. Por ejemplo [2, 1, 2].
 * - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2] y [4, 2, 4]).
"""

def is_boomerang(n, n1, n2):
    if n == n2 and n != n1:
        return True
    return False

def find_boomerangs(array):
    boomerangs = []

    arr_lenght = len(array)
    for i in range(arr_lenght):
        if arr_lenght - i >= 3:
            n = array[i]
            n1 = array[i+1]
            n2 = array[i+2]
            if is_boomerang(n, n1, n2):
                boomerangs.append([n, n1, n2])
        else:
            break

    return boomerangs

def main():
    array = [2, 1, 2, 3, 3, 4, 2, 4]
    boomerangs = find_boomerangs(array)
    print(f"Number of boomerangs in {array}\nTotal: {len(boomerangs)}")
    for boomerang in boomerangs:
        print(boomerang)

if __name__ == '__main__':
    main()