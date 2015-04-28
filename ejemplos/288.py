def maslarga(lista):
  if len(lista)==0:return []
  tam=0
  for i in lista: 
    if len(i)>tam:
      tam=len(i)
  tmp=[]
  for i in lista: 
    if len(i)==tam:
      tmp.append(i)
    
  return tmp

n=int(raw_input("Introduzca el tamano de la lista: "))
V=[0]*n
for i in range(n):
  V[i]=raw_input("Introduzca posicion %d de la lista: "%(i+1))

print "La(s) Cadena(s) más larga(s):"
for i in maslarga(V):
  print i
