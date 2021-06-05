import os
os.system('cls')

def descuento(precio, descuento)->float:
    return precio * ((100 - descuento)/100)

def aplicar_IVA(precio)->float:
    return precio*1.13

def totalizar_lista(lista)->float:
    total=0.0
    for p, d in lista.items():
        p=aplicar_IVA(descuento(float(p), d))
        print("Precio ${:.2f}".format(p), f"Descuento: {d}%")
        total+=p
    return total

#precios y porcentajes
productos={'100':10, '20':20, '30':15, '40':30}

print(f"El total es: {totalizar_lista(productos)}")