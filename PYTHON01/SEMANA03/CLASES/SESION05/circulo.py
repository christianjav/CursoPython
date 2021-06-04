from figura import Figura
from color import Color

class Circulo(Figura, Color):
    def __init__(self, inicio, color, radio):
        Figura.__init__(self, inicio)
        Color.__init__(self, color)
        self.radio=radio

    def calcular_area(self):
        return 3.1416*self.radio**2

circulo=Circulo("mi primer circulo", "verde", 10)
circulo.mostrar_inicio()
circulo.mostrar_color()
print(f"el area es: {circulo.calcular_area():.2f}")