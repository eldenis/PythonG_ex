def espalindromo(cad):
  r=""
  for i in cad:r=i+r  
  return cad==r

cad=raw_input("Dame una palabra: ")
if espalindromo(cad):
  print "La palabra es un palindromo"
else:
  print "La cadena no es un palindromo"