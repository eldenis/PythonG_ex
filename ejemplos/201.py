c=raw_input("Introduzca una cadena: ")

i= int(raw_input("Introduzca el indice para empezar: "))
n= int(raw_input("Introduzca el numero de caracteres: "))

subc=""
for k in range(i,i+n):
  subc+=c[k]
  
print "La subcadena es:",subc