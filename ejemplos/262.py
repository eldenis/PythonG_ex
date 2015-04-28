#mostrar la raiz cubica de un numero
#Ej: la raiz cubica de 8 es 2. y la de 27 es 3
from math import pow

def raiz_cubica(num):  
  return pow(num,1.0/3.0)

num=float(raw_input("Introduzca un numero: "))

print "Raiz cubica de",num,"es",raiz_cubica(num)

  