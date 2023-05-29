# Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.

import re

def count_words(text):
    new_text = re.sub("[^\w\s]", "", text)
    words = new_text.split()
    
    count_dict = {}
    for word in words:
        lower_word = word.lower()
        if lower_word not in count_dict:
            count_dict[lower_word] = 1
        else:
            count_dict[lower_word] += 1

    return count_dict


with open('example_text.txt') as f:
    text = f.read()
print(count_words(text))