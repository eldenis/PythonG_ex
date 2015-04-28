#Calcular la ultima letra del DNI

def ultimaletra(num):
  tmp=0
  for i in num: tmp+= int(i)
  letras="TRWAGMYFPDXBNJZSQVHLCKE"
  return letras[tmp%23]


dni=raw_input("Introduzca el numero del DNI: ")

print "La ultima letra del DNI es:",ultimaletra(dni)
