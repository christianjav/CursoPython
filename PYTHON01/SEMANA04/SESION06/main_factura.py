from cliente import Cliente
from factura import Factura
from imprimir_pdf import ImprimirPDF
from producto import Producto

p1 = Producto("mouse", 4.00, 2)
p2 = Producto("teclado", 6.00, 3)
p3 = Producto("monitor", 60.00, 1)

c1 = Cliente("Alicia", 30)
c2 = Cliente("Beto", 25)

f1 = Factura(Factura.n_factura, '07/06/21', c1)
f2 = Factura(Factura.n_factura, '08/06/21', c2)

f1.agregar_producto(p1)
f1.agregar_producto(p2)

f2.agregar_producto(p1)
f2.agregar_producto(p2)
f2.agregar_producto(p3)


imp = ImprimirPDF()
imp.imprimir(f1)
print("****************************************")
imp.imprimir(f2)
