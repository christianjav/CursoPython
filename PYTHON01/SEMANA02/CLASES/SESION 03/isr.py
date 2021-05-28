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

def calculo_isss(sueldo: float, isss=0.03):
    if sueldo>1000:
        return 1000*0.03
    else:
        return sueldo*0.03

def calculo_afp(sueldo: float, afp=0.0725):
    return sueldo*afp


def calculo_descuentos(sueldo, isss=0.03, afp=0.0725):
    return sueldo - calculo_afp(sueldo) - calculo_isss(sueldo)

def calculo_isr(sueldo):
    sg=calculo_descuentos(sueldo)
    if sueldo<=487.60:
        sg=0.00
    if sueldo>=487.61 and sueldo<=642.85:
        sg=(sg-487.60)*0.1 + 17.48
    if sueldo>=642.86 and sueldo<=915.81:
        sg=(sg-642.85)*0.1 + 32.70
    if sueldo>=915.82 and sueldo<=2058.67:
        sg=(sg-915.82)*0.2 + 60.0
    if sueldo>= 2058.68:
        sg=(sg-2058.68)*0.3 + 288.57
