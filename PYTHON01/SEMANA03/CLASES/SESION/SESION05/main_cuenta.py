from PYTHON01.SEMANA03.CLASES.SESION.SESION05.cuenta import Cuenta
import sys
from cuenta import cuenta

def main():
    menu="""
    ########################
    [1] Crear Cuenta
    [2] Retirar
    [3] Depositar
    [4] Consultar Saldo
    [*] Salir
    ########################
    """

    print(menu)
    op=int(input("Digite una opción: "))
    listaCuentas=[]

    while op>=1 and op<=4:
        numero_cuenta=int(input("Digite el numero de cuenta: "))
        if op==1:
            cliente=input("Digite el nombre del cliente: ")
            c=Cuenta(cliente, numero_cuenta)

            listaCuentas.append(c)
        elif op==4:
            
