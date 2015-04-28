#Programa que lee una cadena y dice cuantas letras mayusculas tiene

def mayusculas(cad):
  res=0
  for i in cad:
    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      res+=1
  return res


lacadena=raw_input('Introduzca una cadena: ')
print 'La cadena tiene %d letras mayusculas' % mayusculas(lacadena)