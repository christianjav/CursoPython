diccionario=  {
    'FK'  : 'Llave'
    ,'PK' : 'Primary Key'
    ,'AK' :  'Auto Increment'
} 

diccionario['FK']= 'Llave foranea'

print(diccionario)

for k, v in diccionario.items():
    print(k, v)

for v in diccionario.values():
    print(v)

del diccionario


d1=  {
    'F'  : {'id':1, 'id2':2}
    ,'P' : 'Primary Key'
    ,'A' :  'Auto Increment'
} 

print('')
