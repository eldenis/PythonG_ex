#Leer una cadena y decir si es un entero

def esentero(x):
  digitos="0123456789"
  for i in x:
    if i not in digitos: 
      return False
  return True

palabra=raw_input("Introduzca una cadena: ")

if esentero(palabra):
  print "Es entero"
else:
  print "NO es entero"
    
    