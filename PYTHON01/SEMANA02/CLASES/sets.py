lenguajes={'c++', 'python', 'java', 'javascript'}

for lenguaje in lenguajes:
    print(lenguaje)

lenguajes.add('python')
print('lenguajes')

lenguajes.add('php')

lenguajes.discard('java')

for lenguaje in lenguajes:
    print(lenguaje)

lenguajes.clear()

#def lenguajes