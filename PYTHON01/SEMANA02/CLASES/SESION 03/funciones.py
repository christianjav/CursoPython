def mi_primera_funcion():
        print('Hola, primera función')


mi_primera_funcion()


def sumar(a, b):
     return a + b

n=sumar(5,7)
print(f"la suma es {n}")

#paso por valor
y=2
def modificar_variable(x):
    x+=20
    return x

modificar_variable(y)
print(f"el valor de y es: {y}")

v=[1, 2, 3]
def modificar_vector(z):
    z.append(4)
    return z
modificar_vector(v)
print(v)


