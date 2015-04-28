def fact(n):
  tmp=1
  if n==0: return tmp
  for i in range(1,n+1):
    tmp=i*tmp
  return tmp

print "Programa que calcula n!"

n=-1
while n<0:
  n=int(raw_input("Introduzca el valor de n: "))

print "\nn!:",fact(n)
