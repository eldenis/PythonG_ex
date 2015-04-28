#Muestra la menor de 5 palabras leidas por teclado
#Sin aceptar que las mayusculas son menores que las minusculas

menor=""
for i in range(5):
  palabra=raw_input("Introduzca una palabra: ")
  if i==0:menor=palabra
  if palabra.upper()<menor.upper():
    menor=palabra

print "La menor palabra de las cinco leidas es: %s"%menor