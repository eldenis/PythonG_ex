def sumatoria(n,m):
  sum=0
  for i in range(n,m+1):
    sum=sum+i
  return sum

print "Programa que calcula la sumatoria de i desde n hasta m\n"
n=int(raw_input("Introduzca el valor de n: "))
m=int(raw_input("Introduzca el valor de m: "))

if n>m:
  print "n debe ser menor o igual a m"
else:
  print "Sumatoria de i:",sumatoria(n,m)
