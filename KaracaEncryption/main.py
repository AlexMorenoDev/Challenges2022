"""
 * Enunciado: Crea una función que sea capaz de encriptar y desencriptar texto utilizando el
 * algoritmo de encriptación de Karaca (debes buscar información sobre él).
"""
import utils


def karaka_encoder(text):
    result = ""

    # Step 1: Reverse the input
    result = utils.reverse_word(text)

    # Step 2: Replace all vowels using the following values
    result = utils.replace_chars(result, {'a': '0', 'e': '1', 'i': '2', 'o': '3', 'u': '4'})
    
    #Step 3: Add 'aca' to the end of the resulting word
    result += 'aca'

    return result


def karaka_decoder(text):
    # Step 1: Remove 'aca' from the end of the input
    text = text[:-3]

    # Step 2: Replace all numbers using the following values
    text = utils.replace_chars(text, {'0': 'a', '1': 'e', '2': 'i', '3': 'o', '4': 'u'})

    #Step 3: Reverse the resulting word
    result = utils.reverse_word(text)

    return result


def main():
    print(karaka_encoder("apple"))
    print(karaka_decoder("1lpp0aca"))


if __name__ == "__main__":
    main()