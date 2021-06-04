from PYTHON01.SEMANA03.CLASES.SESION05.figura import Figura

class Rectangulo(Figura):
    def __init__(self, inicio, base, altura):
        super().__init__(inicio)
        self.base=base
        self.altura=altura

    def calcular_area(self):
        print(self.base * self.altura)

    def calcular_perimetro(self):
        print(self.base + self.altura)*2

r = Rectangulo("primer rectangulo", 10, 20)
r.mostrar_inicio()
print(f"El area es: {r.calcular_area()}")
print(f"El perimetro es: {r.calcular_perimetro()}")

f = Rectangulo("una figura")
f.mostrar_inicio()
