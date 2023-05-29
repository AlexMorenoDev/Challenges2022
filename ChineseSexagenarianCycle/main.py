# Enunciado: Crea un función, que dado un año, indique el elemento y animal correspondiente
# en el ciclo sexagenario del zodíaco chino.
# - Información: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
# - El ciclo sexagenario se corresponde con la combinación de los elementos madera,
#   fuego, tierra, metal, agua y los animales rata, buey, tigre, conejo, dragón, serpiente,
#   caballo, oveja, mono, gallo, perro, cerdo (en este orden).
# - Cada elemento se repite dos años seguidos.
# - El último ciclo sexagenario comenzó en 1984 (Madera Rata).

def chinese_zodiac(year):
    initial_year = 604
    if year < initial_year:
        print("ERROR: Chinese Sexagenarian Cycle started in the year 604!")

    animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig"]
    elements = ["Wood", "Fire", "Earth", "Metal", "Water"]

    # TO DO

    
