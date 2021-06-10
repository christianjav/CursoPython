class Factura:
    n_factura = 0
    def __init__(self, idfactura, fecha, cliente):
        self.__idfactura = idfactura
        self.__fecha = fecha
        self.__cliente = cliente
        self.__lista_productos = []
        Factura.n_factura += 1
        self.__total = 0

    def get_lista_productos(self):
        return self.__lista_productos

    def agregar_producto(self, producto):
        self.__lista_productos.append(producto)
        self.__total += producto.get_precio()*producto.get_cantidad()
        # print(f"producto agregado: {producto}")

    def __str__(self):
        return (
            f'idfactura: {self.__idfactura}\n'
            f'Fecha: {self.__fecha}\n'
            f'{self.__cliente}\n'
            f'Total factura: {self.__total}'
        )