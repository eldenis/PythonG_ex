from math import log

def logb(b,x):
  return log(x,b)

x=float(raw_input("Introduzca el numero al cual sacar el logaritmo: "))
b=float(raw_input("Introduzca la base: "))

print "El logaritmo en base %.2f de %.2f es %f"%(b,x,logb(b,x))