# Enunciado: Crea UNA ÚNICA FUNCIÓN que sea capaz de calcular y retornar el área de un polígono.
# - La función se ejecutará para un tipo de polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

class Polygon:
    def __init__(self):
        self.area = None

    def calculate_area(self):
        pass

    def print_area(self):
        pass

class Square(Polygon):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def calculate_area(self):
        self.area = self.width * self.height

    def print_area(self):
        print("Square area is: {}".format(self.area))

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def calculate_area(self):
        self.area = self.width * self.height

    def print_area(self):
        print("Rectangle area is: {}".format(self.area))

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def calculate_area(self):
       self.area = (self.base * self.height) / 2

    def print_area(self):
        print("Triangle area is: {}".format(self.area))



s = Square(5.0, 5.0)
s.calculate_area()
s.print_area()

r = Rectangle(15.0, 10.0)
r.calculate_area()
r.print_area()

t = Triangle(4.0, 10.0)
t.calculate_area()
t.print_area()
