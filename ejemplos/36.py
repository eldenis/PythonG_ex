#calcular area y perimetro de un triangulo a partir de sus lados

from math import sqrt
a=float(raw_input('Lado a: '))
b=float(raw_input('Lado b: '))
c=float(raw_input('Lado c: '))
perimetro=a+b+c
s=perimetro/2
area=sqrt(s*((s-a)*(s-b)*(s-c)))
print "El perimetro del triangulo es: %0.2f metros"%(perimetro)
print "El area del triangulo es: %0.11f metros cuadrados"%(area)