# Enunciado: Dado un listado de números, encuentra el SEGUNDO más grande.

def find_greatest(lst):
    greatest = 0
    for n in lst:
        if n > greatest:
            greatest = n
    return greatest

def second_greatest(lst):
    if len(lst) == 0:
        print("ERROR: The array doesnt contain anything!")
        return None

    numbers = set(lst)
    if len(numbers) == 1:
        print("ERROR: The array only contains number {}!".format(lst[0]))
        return None

    numbers.remove(find_greatest(numbers))
    return find_greatest(numbers)


print(second_greatest([4, 6, 1, 8, 2])) # 6
print(second_greatest([4, 6, 8, 8, 6])) # 6
print(second_greatest([4, 4, 4])) # Error: only number 4 appears
print(second_greatest([])) # Error: len = 0
