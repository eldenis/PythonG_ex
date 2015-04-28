def ultimaletra(num):
  tmp=0
  for i in num: tmp+= int(i)
  letras="TRWAGMYFPDXBNJZSQVHLCKE"
  return letras[tmp%23]

def eslaletra(letra,dni):
  return letra==ultimaletra(dni)

numero=raw_input("Introduzca el numero del DNI: ")
letra=raw_input("Introduzca la letra DNI: ")
letra=letra.upper()

if eslaletra(letra,numero):
  print "Esa letra pertenece a ese numero de DNI"
else:
  print "Esa letra NO pertenece a ese numero de DNI"