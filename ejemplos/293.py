def sum(a,b):
  if a>b:return 0
  tmp=0
  for i in range(a,b+1):    
    tmp+=i
  return tmp

a=int(raw_input("Introduzca a: "))
b=int(raw_input("Introduzca b: "))

print "Sumatoria =",sum(a,b)