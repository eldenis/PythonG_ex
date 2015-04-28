#Programa que lee una lista de 10 elementos
#compuesta solo de numeros enteros positivos

lista=[0]*10
i=0
while i<10:
  n = int(raw_input("Introduzca un numero entero positivo para la lista: "))
  if n<0:
    print "Numero negativo, no agregado a la lista."
  else:
    lista[i]=n
    i+=1

print lista