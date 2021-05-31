""" 
E5. Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de
apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy" debe
devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1
"""

import os
os.system ("cls")


diccionario = {}
frase = input("Escriba una frase, que repita palabras :")
frase_palabras = frase.lower().split(" ")
for palabra in frase_palabras:
	if palabra in diccionario:
		diccionario[palabra]+=1
	else:
		diccionario[palabra]=1	

for palabra,conteo in diccionario.items():
	print (f"\'{palabra}\':{conteo},",end="")