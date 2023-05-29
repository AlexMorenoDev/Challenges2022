# Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.

def is_anagram(s1, s2):
    s1_lower = s1.lower().replace(" ", "")
    s2_lower = s2.lower().replace(" ", "")

    if len(s1_lower) != len(s2_lower) or s1 == s2:
        return False

    for c in s1_lower:
        if c not in s2_lower:
            return False
    
    return True

print(is_anagram("Debit card", "Bad credit")) # True
print(is_anagram("Dormitory", "Dirty room")) # True
print(is_anagram("The earthquakes", "The queer shakes")) # True
print(is_anagram("Astronomer", "Moon starer")) # True
print(is_anagram("Punishments", "Nine thumps")) # False - one 's' missing
print(is_anagram("car", "rat")) # False - cannot create same word
print(is_anagram("School master", "The classroom")) # True
