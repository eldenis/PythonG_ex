#Leer dos cadenas a y b y decir si b es subcadena de a o no

a=raw_input("Introduzca una cadena: ")
b=raw_input("Introduzca otra cadena: ")

if b in a:
  print b,"es subcadena de",a
else:
  print b,"NO es subcadena de",a
