# Enunciado: Crea una función que reciba un texto y muestre cada palabra en una línea, formando
# un marco rectangular de asteriscos.
# - "¿Qué te parece el reto?" Se vería así:
#   **********
#   * ¿Qué   *
#   * te     *
#   * parece *
#   * el     *
#   * reto?  *
#   **********

def get_max_lenght(words):
    mx = 0
    for word in words:
        current = len(word)
        if current > mx:
            mx = current
    
    return mx

def custom_print(text):
    words = text.split()
    max_l = get_max_lenght(words)

    print(("*"*max_l) + "****")
    for word in words:
        print("* " + word + " "*(max_l-len(word)) + " *")

    print(("*"*max_l) + "****")
    

custom_print("Hello world! Awesome text is being printed out! :)")
#custom_print("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")