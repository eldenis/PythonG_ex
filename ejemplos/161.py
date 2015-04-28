#Programa que lee una cadena y dice si tiene digitos

def digitos(cad):
  for i in cad:
    if i in '0123456789':
      return True
  return False


lacadena=raw_input('Introduzca una cadena: ')
if digitos(lacadena):
  print "Contiene digito"
else:
  print "No contiene digito"