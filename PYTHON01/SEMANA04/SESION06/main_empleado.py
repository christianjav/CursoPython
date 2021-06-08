from empleado import Empleado, EmpleadoPorComision, EmpleadoPorHora

e1=Empleado("Alicia")
e2=EmpleadoPorComision("Beto",1000,0.07)
e3=EmpleadoPorHora("Eva",100,10,5)

print(f"calcular sueldo {e1.calcular_sueldo()}")
print(f"calcular sueldo {e2.calcular_sueldo()}")
print(f"calcular sueldo {e3.calcular_sueldo()}")

if isinstance(e1, Empleado):
    print("si es instancia")

if isinstance(e2, EmpleadoPorComision):
    print("si es instancia")

if isinstance(e3, object):
    print("si es instancia")

if isinstance(e3, Empleado):
    print("si es instancia")

if isinstance(e3, EmpleadoPorHora):
    print("si es instancia")