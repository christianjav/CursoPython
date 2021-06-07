class Cuenta:

    def __init__(self, cliente:str, numeroCuenta:int,saldo:float=0) -> None:
        self.__cliente = cliente
        self.__saldo = saldo
        self.__numeroCuenta = numeroCuenta

    def consultar_saldo(self):
        return self.__saldo

    def buscar_cuenta(self, listaCuentas):
        lista = [c for c in listaCuentas if c.get_numero_cuenta() == self.__numeroCuenta]
        return lista

    def get_numero_cuenta(self):
        return self.__numeroCuenta

    def retirar(self, cantidad):
        if self.__saldo>=cantidad:
            self.__saldo -= cantidad
        else:
            print("Su cuenta no posee suficiente saldo!!")
        return self.__saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad
        return self.__saldo

    def __str__(self):
        return (f'cliente: {self.__cliente}\n'
        f'saldo: {self.__saldo}\n'
        f'cuenta #: {self.__numeroCuenta}\n'
        )

    

