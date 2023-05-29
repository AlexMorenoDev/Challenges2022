# Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
# - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
# - La función recibirá dos String y retornará un Int.
# - La diferencia en días será absoluta (no importa el orden de las fechas).
# - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.

from datetime import date

def calculate_days(date1, date2):
    try:
        d1, m1, y1 = date1.split('/')
        d2, m2, y2 = date2.split('/')

        date1 = date(int(y1), int(m1), int(d1))
        date2 = date(int(y2), int(m2), int(d2))
        delta = date2 - date1
    except:
        print("ERROR: Incorrect date format! The expected format is: DD/MM/YYYY")
        return None

    return abs(delta.days)

print(calculate_days("18/05/2022", "29/05/2022"))
print(calculate_days("18/5/2022", "29/04/2022"))
print(calculate_days("09/09/2023", "09/09/2022"))