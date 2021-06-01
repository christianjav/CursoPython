# class Persona:
#     pass

# print(Persona)

import os
os.system('cls') 

class Persona:
    def __init__(self, nombre, edad, dui):
        self.nombre=nombre
        self.edad=edad
        self.__dui = dui #Priva el acceso a datos
    def mostrar_datos(self):
        print(f"El dato es: {self.nombre} la edad es: {self.edad} el dui es: {self.__dui}")
    
    def get_dui(self):
        return self.__dui
    def set_dui(self, dui):
        self.__dui=dui

persona = Persona("Alicia", 27, '12232323131-1')
print(f'nombre: {persona.nombre}')
print(f'edad {persona.edad}')

persona_Beto= Persona("Beto", 30, '1232312312-2')
print(f'nombre: {persona_Beto.nombre}')
print(f'edad {persona_Beto.edad}')

persona.mostrar_datos()
persona_Beto.mostrar_datos()

persona.set_dui("12345-7")
print(persona.get_dui())