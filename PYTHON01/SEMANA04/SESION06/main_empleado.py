from empleado import EmpleadoPorComision, EmpleadoPorHoras, Empleado

e1 = Empleado("Alicia")
e2 = EmpleadoPorComision("Beto", 1000, 0.07)
e3 = EmpleadoPorHoras("Eva", 100, 10, 5)

print(f"el sueldo para alicia es: {e1.calcular_sueldo()}")
print(f"el sueldo para beto es: {e2.calcular_sueldo()}")
print(f"el sueldo para eva es: {e3.calcular_sueldo()}")

if isinstance(e3, object):
    print("si es instancia")

if isinstance(e3, Empleado):
    print("si es instancia")
    
if isinstance(e3, EmpleadoPorHoras):
    print("si es instancia")    