from cliente import Cliente
from empleado import Empleado
from cliente import Cliente

e = Empleado("Diana")

if e:
    print(e.nombre)
else:
    print("no tiene nombre")

del e

#c = Cliente("Alicia", 30)
#print(int(c))
