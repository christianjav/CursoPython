#EJERCICIO 03
#CALCULAR LA CANTIDAD DE PALABRAS

import os

def limpiar_pantalla():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls') 

limpiar_pantalla()

oracion = input('Digite la oración: ')
oracion = (oracion.lstrip()).rstrip()
palabras=0

for i, letra in enumerate(oracion):
    if letra==" ":
        palabras+=1
    #print(letra)

if len(oracion)>=1:
    if palabras>=1:
        palabras+=1
    else:
        palabras=1

print(f"La oración contiene: {palabras} palabra(s)")