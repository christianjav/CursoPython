import os

if os.name == 'posix':
    _ = os.system('clear')
else:
    # for windows platfrom
    _ = os.system('cls')  

reloj=input("Digite la actual hora del reloj: ")
hora=int(input("Digte las horas a sumar: "))

if len(reloj)==5:    
    relojAux=int(reloj[0:2])    
elif len(reloj)==4:    
    relojAux=int(reloj[0:1])   
else:
    print("La hora no tiene el formato correcto")
    exit()

relojAux=relojAux+(hora%24)
if int(relojAux)>24:
    relojAux=relojAux%24
elif int(relojAux)==24:
    relojAux="00:"
if len(reloj)==5: 
    print("La hora es: ", str(relojAux) + reloj[2:5])
else:
    print("La hora es: ", str(relojAux) + reloj[1:4])
