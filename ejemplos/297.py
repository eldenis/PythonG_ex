#decir si dos numeros son amigos
#la suma de los divisores del primero (excluido el) = segundo y viceversa
#del 1 al 10000
#solo hay cinco pares de numeros amigos
#220 y 284
#1184 y 1210
#2620 y 2924
#5020 y 5564
#6232 y 6368

def sumdiv(n):
  sumatorio = 0
  for i in range(1, (n/2)+1):
    if n % i == 0:
      sumatorio += i
  return sumatorio 


def sonamigos(x,y):
  return (sumdiv(x)==y and sumdiv(y)==x)

print "Introduzca dos numeros para saber si son amigos"
a=int(raw_input("Introduzca a: "))
b=int(raw_input("Introduzca b: "))

if sonamigos(a,b):
  print "Los numeros son amigos"
else:
  print "Los numeros no son amigos"
    