import sys
import os

from cuenta import Cuenta
os.system('cls')
def main():
    menu = """
            Sistema de Cuentas Banco S.A. de C.V.
            *************************************
            [1] Crear cuenta
            [2] Retirar
            [3] Depositar
            [4] Consultar saldo
            [0] Salir
            *************************************
            """
    os.system('cls')
    print(menu)
    opcion = int(input("Seleccione operacion: "))

    listaCuentas = []    
    while(opcion!=0):
        numero_cuenta = int(input("Digite el numero de cuenta: "))
        if opcion==1:
            cliente = input("Digite nombre del cliente: ")                        
            c = Cuenta(cliente, numero_cuenta)
            listaCuentas.append(c)
            print("cuenta creada exitosamente!")
            input()
        elif opcion==2:
            c = Cuenta('', numero_cuenta)
            cuentaEncontrada = c.buscar_cuenta(listaCuentas)
            cantidad = float(input("Digite la cantidad a retirar: ")) 
            cuentaEncontrada[0].retirar(cantidad)
            print(cuentaEncontrada[0])
            input()
        elif opcion==3:
            c = Cuenta('', numero_cuenta)
            cuentaEncontrada = c.buscar_cuenta(listaCuentas)
            cantidad = float(input("Digite la cantidad a depositar: ")) 
            cuentaEncontrada[0].depositar(cantidad)
            print(cuentaEncontrada[0])
            input()
        elif opcion==4:
            c = Cuenta('', numero_cuenta)
            cuentaEncontrada = c.buscar_cuenta(listaCuentas)
            print(cuentaEncontrada[0])
            input()

        os.system('cls')
        print(menu)
        opcion = int(input("Seleccione operacion: "))
    else:
        print("Final de programa")

if __name__=="__main__":
    main()