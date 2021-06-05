import os
import math
os.system('cls')

inmuebles=[ {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
            {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
            {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
            {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
            {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona':'A'}]

def lista_inmuebles(inmuebles, presupuesto, año=2021):
    lista=[]
    for inmueble in inmuebles:
        precio=0.0
        if inmueble.get("zona")=="A":
            precio=(inmueble.get("metros")*1000 + inmueble.get("habitaciones") * 5000 + int(inmueble.get("garaje"))*15000)*(1- (año-inmueble.get("año"))/100)
        elif inmueble.get("zona")=="B":
            precio=(inmueble.get("metros")*1000 + inmueble.get("habitaciones") * 5000 + int(inmueble.get("garaje"))*15000)*(1-(año-inmueble.get("año"))/100)*1.5            
        if precio<=presupuesto:
            inmueble["precio"]=float("{:2f}".format(precio))
            lista.append(inmueble)    
    return lista

presupuesto=float(input("Digite su presupuesto: "))
print("#"*10, "Los inmuebles disponibles para su presupuesto son:", "#"*10)
print(lista_inmuebles(inmuebles, presupuesto))




