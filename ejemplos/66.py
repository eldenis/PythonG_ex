a=int(raw_input("Introduzca a: "))
b=int(raw_input("Introduzca b: "))
if b==a**2:
  print "El segundo es el cuadrado exacto del primero"
elif b<a**2:
  print "El segundo es menor que el cuadrado del primero"
else:
  print "El segundo es mayor que el cuadrado del primero"