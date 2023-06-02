"""
 * Enunciado: ¡Han anunciado un nuevo "The Legend of Zelda"! Se llamará "Tears of the Kingdom"
 * y se lanzará el 12 de mayo de 2023.
 * Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos "The Legend of Zelda" de la historia?
 * Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda que tú selecciones.
 * - Debes buscar cada uno de los títulos y su día de lanzamiento (si no encuentras el día exacto
 *   puedes usar el mes, o incluso inventártelo)
"""
from datetime import datetime

def initialize_games_info():
    names_dict = {}
    dates_dict = {}

    with open('games.txt', 'r') as text_file:
        count = 1
        for line in text_file:
            if line != '\n':
                name, date = line.split('|')
                names_dict[count] = name
                day, month, year = date.rstrip().split('/')
                dates_dict[count] = datetime(int(year), int(month), int(day))
                count += 1

    return names_dict, dates_dict


def show_game_names(names_dict):
    print("The Legend of Zelda games:")
    for key, value in names_dict.items():
        print(f"\t{key}. {value}")


def select_game(input_msg):
    selection = None
    while True:
        try:
            selection = int(input(input_msg))
            if selection > 0 and selection <= 20:
                break
            else:
                print("Invalid input! It must be a number between 1 and 20")
        except:
            print("Invalid input! It must be a number between 1 and 20")

    return selection


def get_dates_difference(lowest_name, lowest_date, highest_name, highest_date):
    result = highest_date - lowest_date
    return f"Between '{lowest_name}' and '{highest_name}' launches passed {result.days} days ({round(result.days/365, 2)} years)"


def time_between_two_zelda_games(g1_name, g1_date, g2_name, g2_date):
    if g1_date > g2_date:
        return get_dates_difference(g2_name, g2_date, g1_name, g1_date)
    elif g1_date < g2_date:
        return get_dates_difference(g1_name, g1_date, g2_name, g2_date)

    return f"Both games were launched at the same time! On '{g1_date}'"


def main():
    game_names_dict, game_dates_dict = initialize_games_info()
    show_game_names(game_names_dict)
    
    g1 = select_game("Select the first game entering the corresponding number:\n")
    g2 = select_game("Select the second game entering the corresponding number:\n")

    if g1 == g2:
        print(f"You selected '{game_names_dict[g1]}' twice. It was launched on '{game_dates_dict[g1].date()}'")
    else:
        print(time_between_two_zelda_games(game_names_dict[g1], game_dates_dict[g1], game_names_dict[g2], game_dates_dict[g2]))


if __name__ == "__main__":
    main()
