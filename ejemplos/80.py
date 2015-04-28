max=0
for i in range(5):
  n=int(raw_input("Introduzca un numero entero positivo: "))
  if n>max:
    max=n

print "El numero maximo es %d" % (max)