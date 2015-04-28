#Programa que muestre todos los multiplos de n entre n y m ambos inclusive

n=int(raw_input("Introduzca n: "))
m=int(raw_input("Introduzca m: "))

for i in range(n,m+1):
  if (i%n)==0:
    print i