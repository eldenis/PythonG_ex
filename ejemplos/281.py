def media(lista):
  if len(lista)==0:return 0
  return sum(lista)/len(lista)

n=int(raw_input("Introduzca el tamano del vector: "))
V=[0]*n
for i in range(n):
  V[i]=int(raw_input("Introduzca posicion %d del vector: "%(i+1)))

print "La media de los elementos del vector es: ",media(V)
