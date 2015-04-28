#Haz un programa que pida el valor de dos enteros n y m
#y que muestre por pantalla la sumatoria de i desde n hasta m

def sumatoria(n,m):
  tmp=0
  for i in range(n,m+1):
    tmp=tmp+i
  return tmp

print "Sumatoria de i desde n hasta m"
n=int(raw_input("Introduzca n: "))
m=int(raw_input("Introduzca m: "))

print "Sumatoria = %d" % sumatoria(n,m)
