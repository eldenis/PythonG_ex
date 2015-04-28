#Programa para calcular el Maximo Comun Divisor de tres numeros

def mayor(a,b,c):
  if (a>b) & (b>c): return a
  if (b>a) & (b>c): return b
  if (c>a) & (c>b): return c

def MCD(a,b,c):
  tmp=0
  for i in range(1,mayor(a,b,c)+1):
    if (a%i==0) & (b%i==0) & (c%i==0):
      tmp=i
  return tmp

a=int(raw_input('Introduzca el valor de A:'))
b=int(raw_input('Introduzca el valor de B:'))
c=int(raw_input('Introduzca el valor de C:'))

print ""
print "El MCD es: ",MCD(a,b,c)
print "Presione enter para salir."
raw_input()