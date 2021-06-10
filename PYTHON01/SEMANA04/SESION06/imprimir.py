class ImprimirPDF:
    def imprimir(self, factura):
        print(factura)
        print("Lista de produtos")
        for p in factura.get_lista_productos():
            print(p)