#grados a radianes
from math import pi

def aradianes(g):  
  return (g*(pi*2.0))/360.0

g=float(raw_input("Introduzca una cantidad de grados: "))

print "La cantidad en radianes es", aradianes(g)
