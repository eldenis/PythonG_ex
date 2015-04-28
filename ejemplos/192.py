def espalindromo(cad):
  c=""
  r=""
  for i in cad:
    if i.upper() in "AÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ":
      r=i+r  
      c=c+i
  return c==r

cad=raw_input("Dame una cadena: ")
if espalindromo(cad):
  print "La cadena es un palindromo"
else:
  print "La cadena no es un palindromo"