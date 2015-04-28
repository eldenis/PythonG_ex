#Programa que lee numeros del teclado hasta que el usuario
#introduzca un numero negativo

may=0
n=0
while n>=0:
  n=int(raw_input("Introduzca un numero: "))
  if n>may:may=n

print "El numero mayor introducido fue: %d" % may