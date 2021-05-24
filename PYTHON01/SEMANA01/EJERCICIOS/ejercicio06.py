import os

if os.name == 'posix':
    _ = os.system('clear')
else:
    # for windows platfrom
    _ = os.system('cls') 

print('\n')
nombre=input('Nombre: ')
dui=input('DUI: ')
horas=int(input('Horas trabajadas: '))
horas_normales = 10
if horas>0 and horas<=40:
    sueldo=horas*40.0
else:
    sueldo = horas_normales * 40 + (horas - 40) * 20

print('------Boleta de Pago---------')
print('Nombre: ', nombre)
print('DUI: ', dui)
print('Total a pagar: ', sueldo)