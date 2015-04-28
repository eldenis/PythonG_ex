#farenheit a centigrados

def afarenheit(c):  
  return ((c*9)/5.0)+32

c=float(raw_input("Introduzca una cantidad de °C: "))

print "°F=", afarenheit(c)
