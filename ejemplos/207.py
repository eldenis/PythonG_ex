#Leer dos cadenas a y b y decir si b es prefijo de a o no

a=raw_input("Introduzca una cadena: ")
b=raw_input("Introduzca el prefijo que desea buscar: ")

if a.startswith(b):
  print b,"es prefijo de",a
else:
  print b,"NO es prefijo de",a
