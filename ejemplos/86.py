from math import log

def n(Ci,Cf,x):
  if Ci==Cf: return 0
  if x==0: return -1
  if Ci==0 or Cf==0: return -1
  if (1+x/100)==0: return -1
  return (float)(log(Cf)-log(Ci))/log((float)(1)+(x/(float)(100)))

ci=float(raw_input("Introduzca el capital inicial: "))
cf=float(raw_input("Introduzca el capital final: "))
x=float(raw_input("Introduzca el interes: "))


anos=n(ci,cf,x)
if anos==-1:
  print "El calculo es imposible"
else:
  print "La cantidad de anos a esperar es: %0.4f"%anos