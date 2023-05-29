# Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.

def time_to_miliseconds(days, hours, minutes, seconds):
    hours += days * 24
    minutes += hours * 60
    seconds += minutes * 60

    return seconds * 1000

print(time_to_miliseconds(0, 0, 0, 10))
print(time_to_miliseconds(2, 5, 45, 10))
print(time_to_miliseconds(2000000000, 5, 45, 10))
