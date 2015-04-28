"""
El area A de un triangulo se puede calcular a 
partir del valor de dos de sus lados, a y b,
y del angulo tita que estos forman entre si con la formula 
1/2*ab*sin(tita). Disena un programa que pida al
usuario el valor de los dos lados (en metros),
el angulo que estos forman (en grados), y
muestre el valor del area.
"""

from math import sin,pi

a=float(raw_input("Introduzca el valor de a: "))
b=float(raw_input("Introduzca el valor de b: "))
tita=float(raw_input("Introduzca el valor de tita: "))
titaradianes=(tita*pi)/180

area=(a*b*sin(titaradianes))/2

print "Area: %f"%(area)