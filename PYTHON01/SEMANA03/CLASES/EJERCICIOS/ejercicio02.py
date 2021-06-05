import os

os.system('cls')

def validar_correo(correo)->bool:
    valido=False
    for i in range(0, len(correo)):
        if correo[i]=='@':
            valido=True
    return valido

print("#"*10,  "Ingrese el nombre y correo del usuario", "#"*20)
nombre = input('Nombre: ')
correo = input('Correo: ')
while not validar_correo(correo):
    print('Correo No valido!!! Ingrese nuevamente el correo')
    correo = input('Correo: ') 

print("Nombre y Correo Validos:")       
print(f"Nombre: {nombre}")
print(f"Correo: {correo}")