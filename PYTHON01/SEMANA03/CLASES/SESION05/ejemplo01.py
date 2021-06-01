import sys

print(sys.argv)
print(f'argumentos sin el nombre del programa {sys.argv[1:]}')

suma=0
lista=sys.argv[1:]

for i in range(len(lista)):
    suma+=int(lista[i])

print(f"La suma es: {suma}")

#