"""
funcion 1/(x+1) en el intervalo [-2,2] con 100 
puntos azules. La funcion es problematica
en x=-1 coordenadas (-1,0) seran un punto
"""
vmen=-2.0
vmay=2.0

window_size(500, 500)
window_coordinates(-5, -5, 5, 5)

x=vmen
intervalo = float((vmay-vmen))/100
f=0.0
create_line(-5,0,5,0,'green')
create_line(0,-5,0,5,'green')
create_point(-1,0,'red')
while x<=vmay:  
  f=float(1.0/(x+1.0))
  create_point(x,f,'blue')
  x+=intervalo