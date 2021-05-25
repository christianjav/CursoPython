import os

if os.name == 'posix':
    _ = os.system('clear')
else:    
    _ = os.system('cls')

lenguajes=['c++', 'python', 'java', 'php']

#print(len(lenguajes))
#print(lenguajes[2])

#x=1
#print(id(x))

#x=2
#print(id(x))
lenguajes.append('c#')
lenguajes.insert(0, 'ruby')

for l in lenguajes:
    print(l)

pruebas=['c++', 1, 'java', True]

for p in pruebas:
    print(p)