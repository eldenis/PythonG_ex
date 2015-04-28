#Programa para calcular el Maximo Comun Divisor de dos numeros

def mayor(a,b):
  if (a>b):
    return a
  return b

def MCD(a,b):
  tmp=0
  for i in range(1,mayor(a,b)+1):
    if (a%i==0) and (b%i==0):
      tmp=i
  return tmp

a=int(raw_input('Introduzca el valor de A:'))
b=int(raw_input('Introduzca el valor de B:'))

print ""
print "El MCD es: ",MCD(a,b)
print "Presione enter para salir."
raw_input()