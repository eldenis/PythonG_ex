#Leer dos cadenas a y b y devolver el prefijo comun mas largo de ambas

a=raw_input("Introduzca una cadena: ")
b=raw_input("Introduzca otra cadena: ")

prefijo=""

for i in range(0,len(a)):
  if a[i]==b[i]:
    prefijo+=a[i]
  else:
    break
  
if prefijo=="":
  print "Las cadenas no tienen prefijos comunes"
else:
  print "El prefijo comun mas largo de ambas es:",prefijo
