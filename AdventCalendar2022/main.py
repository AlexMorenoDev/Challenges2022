"""
 * Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne lo siguiente:
 * - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo de ese día (a tu elección) y cuánto queda para que finalice el sorteo de ese día.
 * - Si la fecha es anterior: Cuánto queda para que comience el calendario.
 * - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.
 *
 * Notas:
 * - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00 y finaliza a las 23:59:59.
 * - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos y segundos.
"""

from datetime import datetime


def initialize_presents():
    presents = []

    with open('presents.txt', 'r') as text_file:
        for line in text_file:
            if line != '\n':
                presents.append(line.rstrip())

    return presents


def get_2022_advent_calendar_present(target_date):
    presents = initialize_presents()
    start_date = datetime(2022, 12, 1, 0, 0, 0)
    end_date = datetime(2022, 12, 24, 23, 59, 59)
    
    if target_date < start_date:
        return f"The advent calendar of 2022 hadn´t started on '{target_date}'. The time remaining was: '{start_date - target_date}'"
    elif target_date > end_date:
        return f"The advent calendar of 2022 had already ended on '{target_date}'. Time passed from its end was: '{target_date - end_date}'"            
    
    return f"The present on '{target_date}' was: '{presents[target_date.day-1]}'"
        
    
def main():
    print(get_2022_advent_calendar_present(datetime(2022, 12, 5, 20, 27, 56)))
    print(get_2022_advent_calendar_present(datetime(2022, 12, 1, 0, 0, 0)))
    print(get_2022_advent_calendar_present(datetime(2022, 12, 24, 23, 59, 59)))
    print(get_2022_advent_calendar_present(datetime(2022, 11, 30, 23, 59, 59)))
    print(get_2022_advent_calendar_present(datetime(2022, 12, 25, 0, 0, 0)))
    print(get_2022_advent_calendar_present(datetime(2022, 10, 30, 0, 0, 0)))
    print(get_2022_advent_calendar_present(datetime(2022, 12, 30, 4, 32, 12)))
    print(get_2022_advent_calendar_present(datetime(2020, 10, 30, 0, 0, 0)))
    print(get_2022_advent_calendar_present(datetime(2024, 12, 30, 4, 32, 12)))


if __name__ == "__main__":
    main()