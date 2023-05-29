# Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
# - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
# - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
# - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

# Sets dont contain repeated values
def get_common_elements(set_1, set_2, get_common):
    result_set = set()
    if get_common:
        # Using intersection function:
        # result_set = set_1.intersection(set_2)
        
        # Not using a function:
        for el in set_1:
            if el in set_2:
                result_set.add(el)
    else:
        # Symmetric difference using xor operator "^":
        result_set = set_1 ^ set_2
       
        # Using symmetric difference function:
        # result_set = set_1.symmetric_difference(set_2)
        
        # Not using a function:
        # for el in set_1:
        #     if el not in set_2:
        #         result_set.add(el)
        # for el in set_2:
        #     if el not in set_1:
        #         result_set.add(el)

    return result_set

print(get_common_elements({1, 2, 3, 3, 4}, {2, 2, 3, 3, 3, 4, 6}, True))
print(get_common_elements({1, 2, 3, 3, 4}, {2, 2, 3, 3, 3, 4, 6}, False))