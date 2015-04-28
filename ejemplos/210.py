#Leer tres cadenas a,b y c y devolver el prefijo comun mas largo de las tres

a=raw_input("Introduzca una cadena: ")
b=raw_input("Introduzca otra cadena: ")
c=raw_input("Introduzca otra cadena: ")

prefijo=""

for i in range(0,len(a)):
  if a[i]==b[i] and b[i]==c[i]:
    prefijo+=a[i]
  else:
    break
  
if prefijo=="":
  print "Las cadenas no tienen prefijos comunes"
else:
  print "El prefijo comun mas largo de las cadenas es:",prefijo
