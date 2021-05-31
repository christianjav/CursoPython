#EJERCICIO05
#PROGRAMA PARA CONTAR PALABRAS REPETIDAS

import os

def limpiar_pantalla():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')

limpiar_pantalla()

diccionario = {}
frase = input("Escriba una frase, que repita palabras: ")
frase_palabras = frase.lower().split(" ")
for palabra in frase_palabras:
	if palabra in diccionario:
		diccionario[palabra]+=1
	else:
		diccionario[palabra]=1	

for palabra,conteo in diccionario.items():
	print (f"\'{palabra}\':{conteo},",end="")