def fact(n):
  if n==0: return 1
  tmp=1
  for i in range(1,n+1):
    tmp=i*tmp
  return tmp

print "Programa que calcula el numero de combinaciones que podemos formar tomando m elementos de un conjunto con n elementos\n"

m=0;n=0
m=int(raw_input("Introduzca el valor de m: "))
while n<m:
  n=int(raw_input("Introduzca el valor de n: "))

CombMN=fact(n)/(fact(n-m)*fact(m))

print "Resultado: ",CombMN
