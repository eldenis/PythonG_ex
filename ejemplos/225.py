n=0
while n<1:
  n=int(raw_input("Introduzca un numero mayor de 1 para el final de la lista: "))

a=range(1,n)

for i in range(0,len(a)):
  a[i]=a[i]**2

print "La lista con los cuadrados es:",a