# Enunciado: Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
# - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".

def get_winner(lst):
    wins = {"R": "S", "S": "P", "P": "R"}

    p1_points = 0
    p2_points = 0
    for el in lst:
        if wins[el[0]] == el[1]:
            p1_points += 1
        elif wins[el[1]] == el[0]:
            p2_points += 1

    if p1_points > p2_points:
        return "Player 1"
    elif p2_points > p1_points:
        return "Player 2"
    else:
        return "Tie"

print(get_winner([("R","S"), ("S","R"), ("P","S")]))
print(get_winner([("S","P"), ("S","P"), ("S","R")]))
print(get_winner([("S","S"), ("P","S"), ("R","S")]))