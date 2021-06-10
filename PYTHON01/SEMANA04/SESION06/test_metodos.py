from empleado import Empleado
from cliente import Cliente

e = Empleado("")

if e:
    print(e.nombre)
else:
    print("no tiene nombre")

del e

c = Cliente("alicia", 30)
print(int(c))

