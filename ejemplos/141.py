"""
140 Haz un programa que, dados tres valores 
a, b y c, muestre la funci´on f(x) = ax2+bx+c
en el intervalo [z1, z2], donde z1 y z2 son
valores proporcionados por el usuario. El
programa de dibujo debe calcular el valor
maximo y minimo de f(x) en el intervalo 
indicado para ajustar el valor de 
window_coordinates de modo que la 
funcion se muestre sin recorte alguno.
"""

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

co=window_coordinates()
create_line(co[0],0,co[2],0,'blue')
create_line(0,co[0],0,co[2],'blue')

x=z1
incremento=(z2-z1)/1000
while x<=z2:
  if int(f(x))==0:    
    print "aqui"
    create_point(x,f(x),'green')
  else:
    create_point(x,f(x),'red')
  x+=incremento