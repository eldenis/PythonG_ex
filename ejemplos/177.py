def esFloat(cad):
  try:
    float(cad)
    return True
  except:
    return False

cad= raw_input("Introduzca una cadena: ")

if esFloat(cad):
  print "La cadena es un valor flotante valido."
else:
  print "La cadena NO es un valor flotante valido."