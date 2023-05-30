
def reverse_word(text):
    result = ""
    for char in reversed(text):
        result += char
    return result


def replace_chars(text, dct):
    for key, value in dct.items():
        text = text.replace(key, value)

    return text
    
