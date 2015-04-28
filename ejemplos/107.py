def sumatoria(n,m):
  sum=0;i=n
  while i<=m:
    sum=sum+i
    i=i+1
  return sum

print "Programa que calcula la sumatoria de i desde n hasta m\n"
n=int(raw_input("Introduzca el valor de n: "))
m=int(raw_input("Introduzca el valor de m: "))

print "Sumatoria de i:",sumatoria(n,m)
