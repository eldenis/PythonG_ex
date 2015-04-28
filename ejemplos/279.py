def cantDeSeries(lista):
  total=0
  ultimo=0
  for i in range(0,len(lista)):
    if i==0:
      total+=1
    elif ultimo!=lista[i]:
      total+=1
    ultimo=lista[i]  
  
  return total

n=int(raw_input("Introduzca el tamano del vector: "))
V=[0]*n
for i in range(n):
  V[i]=int(raw_input("Introduzca posicion %d del vector: "%(i+1)))
  

print "Cantidad de series: ",cantDeSeries(V)