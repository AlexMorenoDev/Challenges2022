# Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

def reverse_string(string):
    r_string = ""

    i = len(string) - 1
    while i >= 0:
        r_string += string[i]
        i -= 1
    
    return r_string

print(reverse_string("Hola mundo"))