def decripto(text):
  cad=""
  for i in text:
    if i in "0123456789":
      if int(i)<2:
        cad+=str(abs(int(i)+8))
      else:
        cad+=str(int(i)-2)
      continue
    if i==" ":cad+=" ";continue
    if i in "ab" or i in "AB":      
      cad+=chr(ord(i)+24)
    else:        
      cad+=chr(ord(i)-2)
  return cad


mensaje=raw_input("Introduzca un texto a desencriptar: ")
print "El mensaje desencriptado es: ",decripto(mensaje)
