#EJERCICIO 01
#CALCULAR SI UNA PALABRA ES PALINDROMO

import os

if os.name == 'posix':
    _ = os.system('clear')
else:
    # for windows platfrom
    _ = os.system('cls') 

palabra = input('Digite la palabra: ')
alreves = ""
j = len(palabra) -1
for i in range(0, len(palabra)):
    alreves = alreves + palabra[j-i]

if (palabra.upper()==alreves.upper()):
    print("Es Palindromo")
else:
    print("No es Palindromo")