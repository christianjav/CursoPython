# programa que usa diccionarios

# Un par llave valor: 
# fk: llave foranea

diccionario = {
    'FK': 'Foreign Key',
    'PK': 'Primary Key',
    'AI': 'Auto Increment'
}

print(diccionario) # imprimir todo
print(diccionario['AI']) # imprimir solo un elemento

diccionario['AI'] = 'AUTO INCREMENT'
print(diccionario) 

# recorrerlo completo
for k, v in diccionario.items():
    print(k,v)

print("--------------------------------------------\n")
# recorrer sólo valores
for v in diccionario.values():
    print(v)

print("FK" in diccionario) 

diccionario.clear()

del diccionario

d1 = {
    'FK': 'Foreign Key',
    'PK': 'Primary Key',
    'AI': 'Auto Increment'
}

d2 = {
    'F': {'id':1,'id2':2},
    'P': 'Primary Key',
    'A': 'Auto Increment'
}


lista = [d1,d2]
print(lista)

# asignar un nuevo elemento
d ={
    "c1": {"p1":"uvas", "p2": "manzanas"},
    "c2": {"p1":"leche", "p2": "cereal"}
}

d["c3"] = {"p1": "huevos","p2":"aceite"}

print(d)