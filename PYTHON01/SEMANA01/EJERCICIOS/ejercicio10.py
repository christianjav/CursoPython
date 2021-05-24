import os

if os.name == 'posix':
    _ = os.system('clear')
else:
    # for windows platfrom
    _ = os.system('cls')

tiempo=input('Ingrese el tiempo que ha estado estaciando el vehículo: ')
horas=0
minutos=0
tarifa=1.5

if len(tiempo)==5:    
    horas=int(tiempo[0:2])
    minutos=int(tiempo[3:5])    
elif len(tiempo)==4:    
    horas=int(tiempo[0:1])
    minutos=int(tiempo[2:4])   
else:
    print("La hora no tiene el formato correcto")
    exit()

if minutos>0:
    fraccion=1*tarifa
if horas>0:
    total=horas*tarifa

total=total+fraccion
print('\n')

print('-----Ticket de Pago--------')
print('Total a Pagar: $',total)
print('horas: ', horas)
print('minutos: ',  minutos)
print('Tiempo total: ', tiempo)
print('---------------------------')