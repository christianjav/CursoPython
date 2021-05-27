import os

if os.name == 'posix':
    _ = os.system('clear')
else:    
    _ = os.system('cls')

lenguajes=['c++', 'python', 'java', 'php']

#print(len(lenguajes))
#print(lenguajes[2])

#x=1
#print(id(x))

#x=2
#print(id(x))
lenguajes.append('c#')
lenguajes.insert(0, 'ruby')

for l in lenguajes:
    print(l)

pruebas=['c++', 1, 'java', True]

for p in pruebas:
    print(p)

######################################################################
######################################################################

#  programa que usa listas
lenguajes = ['c++','python','java','javascript']

print(len(lenguajes))
print(lenguajes[3])

#print(id(lenguajes))
lenguajes[1] = "c"
#print(id(lenguajes))
print(lenguajes[1])

# agregar elemento en lista
lenguajes.append("c#")

print("***********************\n")

# imprimir lista completa
for l in lenguajes:
    print(l)

# eliminar un elemento
lenguajes.remove("c++")
print(lenguajes)

# agregar un elemento en posición específica, dezplaza los otros elementos
lenguajes.insert(1,"python")
lenguajes.insert(1,"Python")
print(lenguajes)

lenguajes.sort() # ordena
lenguajes.reverse() # ordena invertido
lenguajes.extend([2,3]) # agrega elementos al final del array
print("python" in lenguajes) # devuelve un boolean si está o no el elemento

# vaciar lista
lenguajes.clear()
print(lenguajes)

# borrar lista
del lenguajes