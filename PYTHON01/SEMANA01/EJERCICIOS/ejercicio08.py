import os

if os.name == 'posix':
    _ = os.system('clear')
else:
    # for windows platfrom
    _ = os.system('cls') 

distancia=int(input('Distancia recorrida por el vehículo: '))
montofijo=300000
total=0.00

if distancia<=300:
    total=montofijo
if distancia>300 and distancia<=1000:
    total=montofijo+((distancia-300)*15 )
if distancia>1000:
    total=montofijo+((distancia-300)*15 + (distancia-1000)*10)

print('El total a pagar por alquiler: $', total)

