#area de un circulo
from math import pi,pow

def area_circulo(r):  
  return pi*pow(r,2)

r=float(raw_input("Introduzca el radio del circulo: "))

print "El area del ciruclo es",area_circulo(r)

  