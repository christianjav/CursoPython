class Empleado:

    def __init__(self, nombre):
        self.nombre=nombre

    def calcular_sueldo(self):
        """
        empleado -> sueldo base
        empleadoxcomision -> ventas * comision(porcentaje)
        empleadoxhora -> valor * hora + valor*2 * horas_extras
        """
        return 800


    def __del__(self):
        print("El objeto se eliminó")


    def __bool__(self):
        if self.nombre=="":
            return False
        else:
            return True

class EmpleadoPorComision(Empleado):
    def __init__(self, nombre, ventas, comision):
        super().__init__(nombre)
        self.ventas=ventas
        self.comision=comision

    def calcular_sueldo(self):
        return self.ventas*self.comision

class EmpleadoPorHora(Empleado):
    def __init__(self,nombre,valor,horas,horas_extras):
        super().__init__(nombre)
        self.valor=valor
        self.horas=horas
        self.horas_extras=horas_extras

    def calcular_sueldo(self):
        return self.valor * self.horas + self.valor*2 * self.horas_extras
    

