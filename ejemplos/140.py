"""
140 Haz un programa que, dados tres valores 
a, b y c, muestre la funci�on f(x) = ax2+bx+c
en el intervalo [z1, z2], donde z1 y z2 son
valores proporcionados por el usuario. El
programa de dibujo debe calcular el valor
maximo y minimo de f(x) en el intervalo 
indicado para ajustar el valor de 
window_coordinates de modo que la 
funcion se muestre sin recorte alguno.
"""
"""a=1.0
b=1.0
c=-3.0
z1=-5.0
z2=5.0"""

def f(x):
  return ((a*(x**2))+(b*x)+c)

#Pedir los valores
a=float(raw_input("Introduzca valor de a:"))
b=float(raw_input("Introduzca valor de b:"))
c=float(raw_input("Introduzca valor de c:"))
z1=float(raw_input("Introduzca valor de z1:"))
z2=float(raw_input("Introduzca valor de z2:"))

window_size(500,500)
if f(z1)>f(z2):
  window_coordinates(-f(z1),-f(z1),f(z1),f(z1))
else:
  window_coordinates(-f(z2),-f(z2),f(z2),f(z2))
x=z1
incremento=(z2-z1)/1000
while x<=z2:
  create_point(x,f(x),'purple')
  x+=incremento
