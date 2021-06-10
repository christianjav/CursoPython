class Producto:

    def __init__(self, nombre_producto, 
    precio, cantidad):
        self.__nombre_producto=nombre_producto
        self.__precio = precio
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio=precio
    
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_precio(self):
        return self.__precio
    def get_cantidad(self):
        return self.__cantidad

    def __str__(self):
        return (
            f'producto: {self.__nombre_producto}\n'
            f'precio: {self.__precio}\n'
            f'cantidad: {self.__cantidad}'
        )   
        