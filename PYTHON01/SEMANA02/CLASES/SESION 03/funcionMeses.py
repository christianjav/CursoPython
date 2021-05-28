

def get_dias_mes(mes):
    if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):        
        return 31
    elif (mes==4 or mes==6 or mes==9 or mes==11):
        return 30
    elif (mes==2):
        return 28
    else:
        return 0

print(get_dias_mes(3))


def aritme(a, b):
    return a + b * b -2 +b

r = aritme(5,10)

print(r)

