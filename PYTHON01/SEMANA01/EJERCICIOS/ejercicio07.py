import os

if os.name == 'posix':
    _ = os.system('clear')
else:
    # for windows platfrom
    _ = os.system('cls') 

precio_unitario=10.0

productos=int(input('Ingrese la cantidad de productos a comprar: '))
venta_total=0.0
descuento=0.0
producto_obsequio=0

if productos>36:
    venta_total=productos*precio_unitario
    descuento=venta_total*0.15
    venta_total=venta_total*0.85    
    producto_obsequio=productos//12
elif productos>=0 and productos<=36:
    venta_total=productos*precio_unitario
    descuento=venta_total*0.10
    venta_total=venta_total*0.90

print('El precio por unidad es: ', precio_unitario)
print('Total a pagar: $',   venta_total)
print('Descuento total: $',  descuento)
print('Unidades a obsequiar: ', producto_obsequio)


