#Muestra las Subcadenas de longitud 3 de una cadena

cad=raw_input("Introduzca una cadena: ")

for i in range(0,len(cad),3):
  if len(cad[i:i+3])==3:
    print cad[i:i+3]
  
