import os

if os.name == 'posix':
    _ = os.system('clear')
else:
    # for windows platfrom
    _ = os.system('cls') 

convertir=0
print('-----------------Conversor de Monedas------------------')
print('1. Colones ')
print('2. Dolares ')
print('3. Rublos ')
print('\n')
convertir=int(input('Elija la opción a convertir: '))

print('\n')
obtener=int(input('Elija la opción a obtener: '))

monto=float(input('\nDigite el monto: '))

if convertir==1:
    if obtener==2:
        monto=monto/8.75
    if obtener==3:
        monto=monto/0.12
if convertir==2:
    if obtener==1:
        monto=monto*8.75
    if obtener==3:
        monto=monto*73.46
if convertir==3:
    if obtener==1:
        monto=monto*0.12
    if obtener==2:
        monto=monto/73.46

print("El total es: ",  format(monto, '.2f'))