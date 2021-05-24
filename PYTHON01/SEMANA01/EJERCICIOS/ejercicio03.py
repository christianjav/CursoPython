import os

if os.name == 'posix':
    _ = os.system('clear')
else:
    # for windows platfrom
    _ = os.system('cls')    

numero=float(input("Digite el número: "))

if numero%2==0:
    print("el número es par")
else:
    print("el número es impar")
    