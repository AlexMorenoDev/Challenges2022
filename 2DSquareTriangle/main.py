# Enunciado: Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
# - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.

# Only drawing sides
# option: 0 -> square, 1 -> triangle
def draw_figure(side_lenght, option):
    if side_lenght >= 3:
        i = 0
        if option == 0:
            while i < side_lenght:
                if i == 0 or (i == side_lenght-1):
                    print("*"*side_lenght)
                else:
                    print("*" + (" "*(side_lenght-2)) + "*")

                i += 1
        elif option == 1:
            left_spaces = int(side_lenght/2)-1
            middle_spaces = 1
            while i < (side_lenght/2):
                if i == int(side_lenght/2):
                    print("*"*side_lenght)
                elif i == 0:
                    print(" "*int(side_lenght/2) + "*" + " "*int(side_lenght/2))
                else:
                    print(" "*left_spaces + "*" + " "*middle_spaces + "*")
                    left_spaces -= 1
                    middle_spaces += 2

                i += 1
    else:
        print("ERROR: Side lenght must be 3 or more!")

draw_figure(6, 0)
# Triangle must have odd side lenght
draw_figure(7, 1)

