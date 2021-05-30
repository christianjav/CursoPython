#EJERCICIO 02
#CALCULAR LA POTENCIA DE UN NUMERO

import os

def limpiar_pantalla():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls') 

limpiar_pantalla()

print('Calcular Potencia')
base = int(input('Ingrese la base: '))
exponente = int(input('Ingrese el exponente: '))

resultado=0.0
if not exponente<=-1:
    i=exponente
else:
    i=exponente*-1

if i>0:
    while i>0:
        if i==exponente:
            resultado=base
        elif i==(exponente*-1):
            resultado=base
        else:
            resultado*=base
        i-=1
elif i==0:
    resultado=1

if exponente<=-1:
    resultado=1/resultado

print(f"El número {base} elevado a {exponente} es: {resultado}")




