from math import sqrt

def distancia(x1,y1,x2,y2):
  return sqrt(((x1-x2)**2)+((y1-y2)**2))



x1=float(raw_input("Introduzca la abcisa:"))
y1=float(raw_input("Introduzca la ordenada:"))

for i in range(4):
  print("\n")
  x2=float(raw_input("Introduzca la abcisa:"))
  y2=float(raw_input("Introduzca la ordenada:"))  
  if i==0: 
    cerca1=x2
    cerca2=y2
  if distancia(x1,y1,x2,y2)<distancia(x1,y1,cerca1,cerca2):
    cerca1=x2
    cerca2=y2

print "El punto mas cerca del primer punto (%0.2f,%0.2f): (%0.2f,%0.2f)" %(x1,y1,cerca1,cerca2)