def producto(lista):
  if len(lista)==0:return 0
  tmp=1
  for i in lista:
    tmp*=i
  return tmp

n=int(raw_input("Introduzca el tamano del vector: "))
V=[0]*n
for i in range(n):
  V[i]=int(raw_input("Introduzca posicion %d del vector: "%(i+1)))

print "El producto de los elementos del vector es: ",producto(V)
