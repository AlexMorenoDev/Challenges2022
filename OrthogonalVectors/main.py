# Enunciado: Crea un programa que determine si dos vectores son ortogonales.
# - Los dos array deben tener la misma longitud.
# - Cada vector se podría representar como un array. Ejemplo: [1, -2]

def dot_product(a1, a2):
    return (a1[0] * a2[0]) + (a1[1] * a2[1])

def are_orthogonals(a1, a2):
    if len(a1) != 2 or len(a2) != 2:
        print("ERROR: Both arrays must have 2 elements!")
        return None
    
    if dot_product(a1, a2) == 0:
        return True
    return False

print(are_orthogonals((1, 2), (2, 1)))
print(are_orthogonals((2, 1), (-1, 2)))
