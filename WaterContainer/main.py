"""
 * Enunciado: Dado un array de números enteros positivos, donde cada uno representa unidades
 * de bloques apilados, debemos calcular cuantas unidades de agua quedarán atrapadas entre ellos.
 *
 * - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
 *
 *          ⏹
 *          ⏹
 *   ⏹💧💧 ⏹
 *   ⏹💧⏹⏹💧 ⏹
 *   ⏹💧⏹⏹💧 ⏹
 *   ⏹💧⏹⏹⏹⏹
 *
 *   Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades de agua.
 *   Suponemos que existe un suelo impermeable en la parte inferior que retiene el agua.
 *   En los lados como no se dice nada, se sobreentiende que no hay paredes.
"""

def calculate_water_units(array):
    water_units = 0
    array_length = len(array)

    max_value = 0
    temp_units = 0
    for i in range(array_length):
        current_value = array[i]
        if current_value >= max_value:
            max_value = current_value
            if temp_units > 0:
                water_units += temp_units
                temp_units = 0
        else:
            temp_units += max_value - current_value
    
    max_value = 0
    temp_units = 0
    for i in reversed(range(array_length)):
        current_value = array[i]
        if current_value > max_value:
            max_value = current_value
            if temp_units > 0:
                water_units += temp_units
                temp_units = 0
        elif current_value < max_value:
            temp_units += max_value - current_value


    return water_units


def main():
    print(calculate_water_units([4, 0, 3, 6, 1, 3])) # 7
    print(calculate_water_units([3, 1, 6, 3, 0, 4])) # 7
    print(calculate_water_units([3, 2, 1, 0, 3])) # 6
    print(calculate_water_units([2, 0, 4, 0, 5, 0, 3, 0, 5, 0, 4, 0, 5, 0, 2])) # 31
    print(calculate_water_units([5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5])) # 25
    print(calculate_water_units([1, 2, 1, 0, 1, 2, 3, 2, 1, 2, 3, 0, 2, 1])) # 10
    print(calculate_water_units([2, 1, 3, 1, 2, 1, 4, 1, 4])) # 9
    print(calculate_water_units([1, 3, 2, 1, 2, 0, 4, 1, 2, 4, 1])) # 12
    print(calculate_water_units([3, 0, 2, 1, 4, 0, 2, 3, 2, 1, 4, 2, 5, 1, 3, 1, 2, 0, 2])) # 25
    print(calculate_water_units([1, 2, 4, 3, 3, 3, 2, 1, 1])) # 0
    print(calculate_water_units([1, 0, 2, 0, 3, 0, 4, 0, 1, 0, 4, 0, 3, 0, 2, 0, 1])) # 23
    print(calculate_water_units([5, 0, 4, 1, 3, 0, 3, 1, 4, 0, 5])) # 29
    print(calculate_water_units([2, 0, 3, 1, 5, 3, 5, 1, 3, 0, 2])) # 10
    print(calculate_water_units([5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5])) # 1
    print(calculate_water_units([5, 1, 1, 2, 3, 5, 3, 2, 1, 1, 5])) # 26
    print(calculate_water_units([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) # 4


if __name__ == '__main__':
    main()