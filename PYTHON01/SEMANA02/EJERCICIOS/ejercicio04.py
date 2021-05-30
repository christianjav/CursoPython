#EJERCICIO 04
#AÑADIR DÍAS A FECHA

import os
#DECLARAR VARIABLES
d=""
m=""
y=""
j=0
mesAux=""
meses={'1':31, '2':28, '3':31, '4':30,'5':31,'6':30,'7':31,'8':31, '9':30, '10':31, '11':30, '12':31}

def limpiar_pantalla():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')

def Bisiesto(n): 
    if (n%400==0 or (n%4==0 and not(n%100==0))):
        meses["2"]=29
    else:
        meses["2"]=28

limpiar_pantalla()
print("#"*20, "Ingresar Días", "#"*20)
print("#"*55)
fecha=input("Digite la fecha: ")
dias=int(input("Digite los días a adicionar: "))
    
if fecha.find("/")==0:
    print("La fecha no contiene un formato valido")
    exit()

for i, letra in enumerate(fecha):
    if j==0 and letra!="/":
        d+=letra
    if j==1 and letra!="/":
        m+=letra
    if j==2 and letra!="/":
        y+=letra
    if letra=="/":
        j+=1

d=int(d)
m=int(m)
y=int(y)
d+=dias
mesAux=str(m)

continuar=True
while (continuar):
    for mes, dias_mes in (meses.items()):
        if mes==mesAux:
            if d>dias_mes:
                d-=dias_mes
                mesAux= str(int(mesAux) + 1)
        if d<=dias_mes:
            continuar=False
        if int(mesAux)==13:
            mesAux="1"
            y+=1
            Bisiesto(y)
            continuar=True
            
print(f"La fecha es: {d}/{mesAux}/{y}")