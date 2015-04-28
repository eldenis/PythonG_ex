

def es_perfecto(n):
  sumatorio = 0
  for i in range(1, (n/2)+1):
    if n % i == 0:
      sumatorio += i
  return sumatorio == n

print "Muestra los numeros perfectos que hay entre 1 y n"
n=int(raw_input("Introduzca n:"))

print "Los numeros perfectos entre 1 y n son:\n"
for i in range(1,n):
  if es_perfecto(i): print i    

print "\nFIN"
