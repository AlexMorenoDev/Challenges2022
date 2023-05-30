"""
 * Enunciado: Crea una función que sea capaz de detectar y retornar todos los handles de un texto usando solamente Expresiones Regulares.
 * Debes crear una expresión regular para cada caso:
 * - Handle usuario: Los que comienzan por "@"
 * - Handle hashtag: Los que comienzan por "#"
 * - Handle web: Los que comienzan por "www.", "http://", "https://" y finalizan con un dominio (.com, .es...)
"""
import re


def handler_detector(text):
    result = {}
    result['User'] = re.findall('@\w*', text)
    result['Hashtag'] = re.findall('#\w*', text)
    
    web_search = re.findall('((www\.|http\:\/\/|https\:\/\/)\w*\.(com|es|net|de|cn|uk|org|info|eu|nl|ru)(\w|\/)*)', text)
    # Post processing because 're.findall' function returns multiple matches for each group
    result['Web'] = []
    for element in web_search:
        result['Web'].append(element[0])

    return result


def main():
    print(handler_detector("En esta actividad de @mouredev, resolvemos #retos de #programacion desde https://retosdeprogramacion.com/semanales2022, que @braismoure aloja en www.github.com"))


if __name__ == "__main__":
    main()