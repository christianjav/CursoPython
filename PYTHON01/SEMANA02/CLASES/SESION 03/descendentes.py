def descendente(n):
    print(n)
    n=n-1    
    if n>0:
        descendente(n)

n=int(input("Digite un número: "))
descendente(n)            