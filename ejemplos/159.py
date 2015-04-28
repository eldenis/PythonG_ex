#Programa que lee una cadena y dice cuantos espacios en blanco contiene

def espacios(cad):
  res=0
  for i in cad:
    if i==' ':
      res+=1
  return res

lacadena=raw_input('Introduzca una cadena: ')

print 'La cadena tiene %d espacios en blanco' % espacios(lacadena)