# Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
# - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.

def get_output(str1, str2):
    output = ""
    for c in str1:
        if c not in str2:
            output += c

    return output

# Remove characters from str1 if str2 contains them and vice versa 
def removing_characters(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    out1 = get_output(str1, str2)
    out2 = get_output(str2, str1)

    print("Output 1: " + out1)
    print("Output 2: " + out2)
    print("------------------")

removing_characters("hello", "alex")
removing_characters("h", "a")
removing_characters("crocodile", "turtle")

