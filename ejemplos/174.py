#Leer una cadena por teclado y decir cuantos numeros tiene

def esnumero(x):
  digitos="0123456789"
  for i in x:
    if i not in digitos: 
      return False
  return True


palabras=raw_input("Introduzca una cadena: ").split()
cont=0
for i in palabras:
  if esnumero(i):
    cont+=1
    
print "La cadena tiene %d numeros"%(cont)