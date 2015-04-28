#Leer una cadena por teclado y decir cuantos digitos tiene

digitos="0123456789"

cadena=raw_input("Introduzca una cadena: ")
cont=0
for i in cadena:
  if i in digitos:
    cont+=1
    
print "La cadena tiene %d digitos"%(cont)