import os

os.system('cls')

def relacion(a, b):
    if a>b:
        return 1
    if a<b:
        return -1
    if a==b:
        return 0

def main():
    print("La relación entre 5 y 10 es: ", relacion(5,10))
    print("La relación entre 10 y 5 es: ", relacion(10,5))
    print("La relación entre 5 y 5 es: ", relacion(5,5))
    
if (__name__=='__main__'):
    main()