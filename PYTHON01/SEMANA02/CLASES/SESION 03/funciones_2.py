#formas de documentar
#valores por default

def calculo_desc(sueldo: float, isss:float=0.03, afp=0.0725)->float:
    """
    La función calculo_desc se encarga de recibir el salario bruto y retornar el salario gravable
    el paramatro isss es opciona y por default tiene 3%\n
    el parametro afp es opcional y por defecto tiene 7.25%
    """

    sueldo_g=sueldo-sueldo*isss - sueldo*afp
    return sueldo_g

sg= calculo_desc(600, afp=0.08)
print(f"el sueldo gravable es {sg}")

print(type(sg))
print(calculo_desc.__doc__)

def listar_nombres(*nombres):
    for n in nombres:
        print(f"El nombres es: {n}")

listar_nombres("alicia", "beto", "carlos", "diana")

def listar_diccionario(**terminos):
    #for v in terminos.values():
    for k, v in terminos.items():
        print(f"La llave es {k} El valor es: {v}")

listar_diccionario(PK="Llave primar", FK="Llave foranea")

