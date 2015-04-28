from math import pi, cos,sin

x1 = float(raw_input("Dime el limite inferior del intervalo: "))
x2 = float(raw_input("Dime el limite superior del intervalo: "))
puntos = int(raw_input("Dime cuantos puntos he de mostrar: "))

window_size(500, 500)
window_coordinates(x1, -1.5, x2, 1.5)

incremento = (x2 - x1) / puntos

x = x1
while x <= x2 - incremento:
  create_line(x, cos(x), x+incremento, cos(x+incremento))
  create_line(x, sin(x), x+incremento, sin(x+incremento))
  x += incremento