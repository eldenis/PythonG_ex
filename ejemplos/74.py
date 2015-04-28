letra=raw_input("Introduzca una letra: ")

if ord(letra) >=65 and ord(letra)<=90:
  print "La letra es mayuscula"
elif ord(letra)>=97 and ord(letra)<=122:
  print "La letra es minuscula"
elif ord(letra)==241:
  print "Es una eñe minuscula"
elif ord(letra)==209:
  print "Es una eñe mayuscula"    
else:
  print "No es una letra"
