#raiz enesima x a la 1/n

from math import pow

def raiz_n_esima(x,n):
  return pow(x,1.0/n)


x=float(raw_input("Introduzca el numero al que sacar la raiz: "))
n=int(raw_input("Introduzca la base de la raiz: "))
print "resultado:", raiz_n_esima(x,n)