import os
if os.name == 'posix':
    _ = os.system('clear')
else:
    _ = os.system('cls')

#crear una factura solicite n productos y el nombre del cliente
#crear un diccionario que contenga los productos y el cliente
#Pueden haber varias facturas

venta={}


cliente=input('Ingrese el nombre del cliente: ')

venta