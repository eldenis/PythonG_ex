lista=[1,2,1,5,0,3]

i=0
e=0
fin=len(lista)
while i < fin:  
  if i%2==0:
    del lista[e]
    e+=1
  i+=1
  
print "La lista sin los valores en posicion par es:",lista