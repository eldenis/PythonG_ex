#radianes a grados
from math import pi

def agrados(r):  
  return ((r*360)/(pi*2.0))

r=float(raw_input("Introduzca una cantidad en radianes: "))

print "La cantidad en grados es", agrados(r)
