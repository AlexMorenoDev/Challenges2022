"""
 * Enunciado: Calcula dónde estará un robot (sus coordenadas finales) que se encuentra en una cuadrícula
 * representada por los ejes "x" e "y".
 * - El robot comienza en la coordenada (0, 0).
 * - Para idicarle que se mueva, le enviamos un array formado por enteros (positivos o negativos)
 *   que indican la secuencia de pasos a dar.
 *  - Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos, se detiene, luego 5, se detiene,
 *    y finalmente 2. El resultado en este caso sería (x: -5, y: 12)
 * - Si el número de pasos es negativo, se desplazaría en sentido contrario al que está mirando.
 * - Los primeros pasos los hace en el eje "y". Interpretamos que está mirando hacia la parte
 *   positiva del eje "y".
 * - El robot tiene un fallo en su programación: cada vez que finaliza una secuencia de pasos gira
 *   90 grados en el sentido contrario a las agujas del reloj.
"""

def find_robot_coordinates(moves):
    # x and y
    result = [0, 0]
    # y, -x, -y, x
    signs = [1, -1, -1, 1]

    for i in range(len(moves)):
        result[(i+1)%2] += (moves[i] * signs[i%4])

    return tuple(result)


def main():
    print(find_robot_coordinates([10, 5, -2]))
    print(find_robot_coordinates([0, 0, 0]))
    print(find_robot_coordinates([]))
    print(find_robot_coordinates([-10, -5, 2]))
    print(find_robot_coordinates([-10, -5, 2, 4, -8]))
    

if __name__ == "__main__":
    main()