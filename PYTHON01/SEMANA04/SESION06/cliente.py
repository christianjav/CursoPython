class Cliente:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def __str__(self):
        return (
            f'Cliente: {self.__nombre}\n'
            f'Edad: {self.__edad}'
        )

    def __int__(self):
        return self.__edad