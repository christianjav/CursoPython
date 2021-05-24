import os

if os.name == 'posix':
    _ = os.system('clear')
else:
    # for windows platfrom
    _ = os.system('cls')

print('----Calcular Nota------') 
nota1=float(input('Ingrese la nota 1: '))
nota2=float(input('Ingrese la nota 2: '))
nota3=float(input('Ingrese la nota 3: '))
nota4=float(input('Ingrese la nota 4: '))

if nota1<nota2 and nota1>nota3 and nota1<nota4:
    nota_promedio=(nota2+nota3+nota4)/3
if nota2<nota1 and nota2>nota3 and nota2<nota4:
    nota_promedio=(nota1+nota3+nota4)/3
if nota3<nota1 and nota3>nota2 and nota3<nota4:
    nota_promedio=(nota1+nota2+nota4)/3
if nota4<nota1 and nota4>nota2 and nota4<nota3:
    nota_promedio=(nota2+nota3+nota4)/3

print('La nota promedio es: ', format(nota_promedio, '.2f'))