def leerLista():
  tmp=[]
  cad= raw_input("Introduzca una lista separada por comas: ")
  lista=cad.split(",")
  for i in lista:
    tmp.append(int(i))
  return tmp

a=leerLista()

for i in range(0,len(a)):
  if a[i]<0:a[i]=0

print a