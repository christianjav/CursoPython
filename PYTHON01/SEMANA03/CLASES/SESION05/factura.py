class Factura:

    cant_facturas=1

    def __init__(self, cliente, total, n_factura):
        self.cliente=cliente
        self.total=total
        self.n_factura=n_factura
        Factura.cant_facturas+=1

    def __str__(self):
        return('*******************************'
              f'\n N factura: {self.n_factura}'
              f'\n Total:     {self.total}'
              f'\n Cliente:   {self.cliente} \n'
        )

    @classmethod
    def mostar_cant_facturas(cls):
        print(f"La cantida de facturas es: {cls.cant_facturas}")
        #print(f"cliente es: {cls.cliente}")

    @staticmethod
    def sumar_facturas(lista_facturas):
        total_ventas=0
        for f in lista_facturas:
            total_ventas+=f.total

        return total_ventas

print(Factura.cant_facturas)
f1=Factura('Carlos', 100, Factura.cant_facturas)
print(Factura.cant_facturas)
f2=Factura('Diana', 200, Factura.cant_facturas)
print(Factura.cant_facturas)
f3=Factura('Eva', 300, Factura.cant_facturas)
#Factura.cant_facturas=4
#print(Factura.cant_facturas)
#print(f"La cantidad de facturas es {f1.cant_facturas}")
#print(f"La cantidad de facturas es {f2.cant_facturas}")
print(f1)
print(f2)
Factura.mostar_cant_facturas()

lista=[f1, f2, f3]
print(f'el total de factura es: {Factura.sumar_facturas(lista):.2f}')