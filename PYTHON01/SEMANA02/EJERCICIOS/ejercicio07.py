#EJERCICIO05
#PROGRAMA PARA ORDENAR NUMEROS

import os

def limpiar_pantalla():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')

limpiar_pantalla()

lista=[]
print("#"*20,"Programa para ordenar una lista de números","#"*20)
print("Digite * para salir")
continuar=True
while continuar:
    numero=input("Ingrese un número: ")
    if numero=="*":
        continuar=False
    elif numero.isdigit():
        lista.append(int(numero))
temp=0
for j in range (0, len(lista)):
    for i in range (0, len(lista)):
        if i<len(lista)-1:
            if lista[i]>lista[i+1]:
                temp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp

print("Lista ordenada: ")
for i in range (0, len(lista)):
        print(lista[i])