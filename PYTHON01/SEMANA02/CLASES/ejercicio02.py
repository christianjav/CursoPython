# MULTIPLICACION RUSA
x=int(input("Digite el multiplicando: "))
n=int(input("Digite el multiplicador: "))

suma=0
continuar=True
while continuar:
    if not x%2==0:
        suma+=n

    #print(x)
    print(n)
    x=x//2
    n=n*2

    if x<1:
        continuar=False

print('La suma es: ', suma)
