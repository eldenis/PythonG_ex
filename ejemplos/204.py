#Mostrar todos los prefijos de una cadena. 
#EJ: Si la cadena es UJI El programa debe mostrar
#U
#UJ
#UJI

cad=raw_input("Introduzca una cadena: ")

print "Los prefijos de la cadena son:"

tmp=""

for c in cad:
  tmp+=c
  print tmp