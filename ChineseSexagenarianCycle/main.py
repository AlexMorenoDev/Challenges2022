# Enunciado: Crea un función, que dado un año, indique el elemento y animal correspondiente
# en el ciclo sexagenario del zodíaco chino.
# - Información: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
# - El ciclo sexagenario se corresponde con la combinación de los elementos madera,
#   fuego, tierra, metal, agua y los animales rata, buey, tigre, conejo, dragón, serpiente,
#   caballo, oveja, mono, gallo, perro, cerdo (en este orden).
# - Cada elemento se repite dos años seguidos.
# - El último ciclo sexagenario comenzó en 1984 (Madera Rata).

def chinese_sexagenarian_cycle_calculator(year):
    initial_year = 604
    if year < initial_year:
        return "ERROR: Chinese Sexagenarian Cycle started in the year 604!"

    animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig"]
    elements = ["Wood", "Fire", "Earth", "Metal", "Water"]

    subs_result = year - initial_year
    year_animal = animals[subs_result%len(animals)]
    year_element = elements[int((subs_result/2)%len(elements))]
    
    return f"Chinese Sexagenarian Cycle --> Year {year}:\n- Animal: {year_animal}\n- Element: {year_element}"


def main():
    print(chinese_sexagenarian_cycle_calculator(1946))
    print(chinese_sexagenarian_cycle_calculator(1984))
    print(chinese_sexagenarian_cycle_calculator(604))
    print(chinese_sexagenarian_cycle_calculator(603))
    print(chinese_sexagenarian_cycle_calculator(1987))
    print(chinese_sexagenarian_cycle_calculator(2022))
    print(chinese_sexagenarian_cycle_calculator(664))
    print(chinese_sexagenarian_cycle_calculator(1143))
    print(chinese_sexagenarian_cycle_calculator(1678))


if __name__ == "__main__":
    main()

    
