def empiezaConMinuscula(cadena):
  return cadena[0] in "abcdefghijklmnopqrstuvwxyz"

cad=raw_input("Introduzca una cadena: ")

if empiezaConMinuscula(cad):
  print "La cadena empieza con minuscula"
else:
  print "La cadena NO empieza con minuscula"