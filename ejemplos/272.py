def esRepeticion(cadena):
  if len(cadena)%2!=0: return False
  return cadena[0:len(cadena)/2]==cadena[len(cadena)/2:len(cadena)]

cad=raw_input("Introduzca una cadena: ")


if esRepeticion(cad):
  print "La cadena es una repeticion"
else:
  print "La cadena NO es una repeticion"
