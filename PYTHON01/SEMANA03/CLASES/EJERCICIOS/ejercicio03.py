import os

os.system('cls')


def titulo(nombre)->str:
    indice=0
    titulo=""
    l=""
    for i in range(0, len(nombre)):
        l=nombre[i]
        if nombre[i]==" ":
            indice=i+1
        elif i==indice:
            l=l.upper()
                     
        titulo+=l
    return titulo


nombre=input("Digite un titulo: ")
print(titulo(nombre))