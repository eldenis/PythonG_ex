def seriemaslarga(lista):
  ultimo=0
  indice=0
  tammasgrande=0
  indicemasgrande=0
  for i in range(0,len(lista)):
    if i !=0:
      if ultimo != lista[i]:
        tamano=i-indice
        if tamano>tammasgrande:
          tammasgrande=tamano
          indicemasgrande=indice
        indice=i
      elif i==(len(lista)-1):
        tamano=i-indice+1
        if tamano>tammasgrande:
          tammasgrande=tamano
          indicemasgrande=indice
    ultimo=lista[i]
  return indicemasgrande

n=int(raw_input("Introduzca el tamano del vector: "))
V=[0]*n
for i in range(n):
  V[i]=int(raw_input("Introduzca posicion %d del vector: "%(i+1)))

print "La serie mas larga comienza en el indice: ",seriemaslarga(V)
