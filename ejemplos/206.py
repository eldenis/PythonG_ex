#Muestra las Subcadenas de longitud k de una cadena

cad=raw_input("Introduzca una cadena: ")
k=int(raw_input("Introduzca el numero de caracteres de las subcadenas: "))

for i in range(0,len(cad),k):
  if len(cad[i:i+k])==k:
    print cad[i:i+k]
  
