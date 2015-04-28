lista=[1,-2,1,-5,0,3]

i=0

while i < len(lista):  
  if lista[i]%2==0:
    del lista[i]
    i-=1
  i+=1
  
print "La lista sin los valores pares es:",lista