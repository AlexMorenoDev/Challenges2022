"""
 * Enunciado: Crea un función que reciba un texto y retorne la vocal que más veces se repita.
 * - Ten cuidado con algunos casos especiales.
 * - Si no hay vocales podrá devolver vacío.
"""

def find_most_common_vowel(text):
    vowels = {
        'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0
    }
    text = text.lower()
    text = text.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ü', 'u')

    for char in text:
        if char in vowels:
            vowels[char] += 1

    result = []
    max_value = max(vowels.values())
    
    for key, value in vowels.items():
        if value != 0 and value == max_value:
            result.append(key)

    return result


def main():
    print(find_most_common_vowel("aaaaaeeeeiiioou"))
    print(find_most_common_vowel("AáaaaEeeeIiiOoU"))
    print(find_most_common_vowel("eeeeiiioouaaaaa"))
    print(find_most_common_vowel(".-Aá?aaaBbEeeweIiiOoU:"))
    print(find_most_common_vowel(".-Aá?aaa BbEeew eIiiOoU:"))
    print(find_most_common_vowel(".-Aá?aaa BbEeew eEIiiOoU:"))
    print(find_most_common_vowel(".-Aá?aaa BbEeew eEIiiOoUuuuuu:"))
    print(find_most_common_vowel("aeiou"))
    print(find_most_common_vowel("brp qyz"))
        

if __name__ == "__main__":
    main()