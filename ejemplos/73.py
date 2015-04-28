letra=raw_input("Introduzca una letra: ")

if ord(letra) >=65 and ord(letra)<=90:
  print "La letra es mayuscula"
elif ord(letra)>=97 and ord(letra)<=122:
  print "La letra es minuscula"
else:
  print "No es una letra"
