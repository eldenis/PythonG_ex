vocmin="aeiou"
vocmay="AEIOU"
conmin="bcdfghjklmnpqrstvwxyz"
conmay="BCDFGHJKLMNPQRSTVWXYZ"

c=raw_input("Introduzca un caracter: ")

if c in vocmin:
  print "El caracter es una vocal minuscula"
elif c in vocmay:
  print "El caracter es una vocal mayuscula"
elif c in conmin:
  print "El caracter es una consonante minuscula"
elif c in conmay:
  print "El caracter es una consonante mayuscula"
else:
  print "El caracter es otro"

