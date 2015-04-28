def maslarga(lista):
  if len(lista)==0:return ""
  indice=0
  for i in range(len(lista)):
    if len(lista[i])>len(lista[indice]):
      indice=i
  return lista[indice]

n=int(raw_input("Introduzca el tamano de la lista: "))
V=[0]*n
for i in range(n):
  V[i]=raw_input("Introduzca posicion %d de la lista: "%(i+1))

print "La cadena mas larga de la lista es:",maslarga(V)
