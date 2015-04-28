def sol(a,b):
  if a==0 :return "None"
  return -b/a

print "Soluciona ax + b = 0"
a=float(raw_input("Introduzca a: "))
b=float(raw_input("Introduzca b: "))

print "x=",sol(a,b)