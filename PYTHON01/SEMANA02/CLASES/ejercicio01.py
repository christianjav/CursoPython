x=int(input("Digite el número: "))
n=int(input("Digite la potencia: "))
total=0

i=1
for i in range(n):
    if i==1:
       total=x*x
    else:
        total*=x
    i+=1

print('Con for',total)


i=1
while i<=(n-1):
    if i==1:
       total=x*x
    else:
        total*=x
    i+=1

print('Con while', total)
   
