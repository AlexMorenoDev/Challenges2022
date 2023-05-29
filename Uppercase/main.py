# Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
# poner en mayúscula la primera letra de cada palabra.
# - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

def custom_uppercase(text):
    words = text.split()     
    formatted_words = []
    for word in words:
        formatted_words.append(word[0].upper() + word[1:])

    return ' '.join(formatted_words)

# Alternative implementation (slowlier)
def custom_uppercase_2(text):
    text = text[0].upper() + text[1:]
    
    uppercase = False
    formatted_text = ""
    for c in text:
        if uppercase:
            formatted_text += c.upper()
            uppercase = False
        else:
            formatted_text += c
        if c == ' ':
            uppercase = True

    return formatted_text

print(custom_uppercase("hello, my name is alex"))      
print(custom_uppercase_2("hello, my name is alex"))