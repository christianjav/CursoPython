from abc import ABC, abstractmethod

class Persona(ABC):

    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    
    @abstractmethod
    def mostrar_datos(self):
        pass

class Empleado(Persona):

    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo=sueldo

    def mostrar_datos(self):
        print(f"nombre: {self.nombre}"
              f"edad: {self.edad}"  
              f"sueldo: {self.sueldo}"
        )

e = Empleado('Alicia', 30, 800)
e.mostrar_datos()

# class Conexion(ABC):
#     @abstractmethod
#     def conectar():
#         pass

#     @abstractmethod
#     def desconectar():
#         pass

# class ConexionOracle(Conexion):
#     pass