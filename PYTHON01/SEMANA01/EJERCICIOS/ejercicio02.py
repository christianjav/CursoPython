renta=0.00
print('Calculo de Renta \\n')
salario=float(input('Ingrese su salario: '))

if (salario>0):
    isss=salario*0.03
    if isss>30:
        isss=30

    afp=salario*0.0725

sg=salario-isss-afp

if sg<=487.60:
    renta=0.00
if sg>=487.61 and sg<=642.85:
    renta=(sg-487.60)*0.1 + 17.48
if sg>=642.86 and sg<=915.81:
     renta=(sg-642.85)*0.1 + 32.70
if sg>=915.82 and sg<=2058.67:
     renta=(sg-915.82)*0.2 + 60.0
if sg>= 2058.68:
    renta=(sg-2058.68)*0.3 + 288.57
print('La renta es de: ', renta)