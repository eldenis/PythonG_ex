#Programa que muestra todos los numeros pares entre 2 y n
#donde n es un numero introducido por teclado

n=int(raw_input("Introduzca un numero: "))

for i in range(2,n+1):
  if (i%2)==0:
    print i