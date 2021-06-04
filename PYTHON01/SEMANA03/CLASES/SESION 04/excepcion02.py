#http://www.sharetxt.live/
try:
    a=30
    b=20
    if a>b:
        raise Exception("Error", "El primer numero es mayor que el segundo")
except Exception as e:
    print("ocurrio un error: ", e)