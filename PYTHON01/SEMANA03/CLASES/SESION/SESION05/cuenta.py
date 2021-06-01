class Cuenta:
    def __init__(self, cliente, numeroCuenta:int, saldo:float=0.0)->None:
        self.__cliente=cliente
        self.__saldo=saldo
        self.__numeroCuenta=numeroCuenta

    def consultar_saldo(self):
        return self.__saldo
        # lista=[c for c in listaCuentas if c.numeroCuenta==numeroCuenta]
        # return lista[0]=get_salado()

    def buscar_cuenta(self, listaCuentas, numeroCuenta):
        lista=[c for c in listaCuentas if c.numeroCuenta==numeroCuenta]
        return lista        

    def retirar(self, cantidad):
        self.__saldo-=cantidad
        return  self.__saldo

    def depositar(self,cantidad):
        self.__saldo+=cantidad
        return  self.__saldo

    def __str__(self):
        return(f'cliente: {self.__cliente}')
        