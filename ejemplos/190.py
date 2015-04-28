def esalf(cad):
  for i in range(0,len(cad)-1):
    if cad[i]>cad[i+1]:
      return False
  return True


cad=raw_input("Introduzca una palabra: ")

if esalf(cad):
  print "La palabra es alfabetica"
else:
  print "La palabra NO es alfabetica"  