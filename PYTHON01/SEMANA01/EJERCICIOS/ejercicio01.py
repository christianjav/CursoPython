#EJERCICIO 01
#CALCULAR SI UN AÑO ES BISIESTO

import os

if os.name == 'posix':
    _ = os.system('clear')
else:
    # for windows platfrom
    _ = os.system('cls') 

n=int(input("Ingrese el año: "))

if (n%4==0 or (n%400==0 and not(n%100==0))):
    print('el año es bisiesto')
else:
    print('el año no es bisiesto')