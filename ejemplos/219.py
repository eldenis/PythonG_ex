#lee dos listas y dice si la primera es mayor que la segunda
def leerLista():
  tmp=[]
  for i in raw_input("Introduzca una lista separada por comas: ").split(","):    
    tmp.append(int(i))
  return tmp
  
a=leerLista()
b=leerLista()

valA=0
valB=0

for i in a:valA +=i
for i in b:valB +=i

if valA>valB:
  print "La primera lista es mayor que la segunda"
else:
  print "La primera lista NO es mayor que la segunda"