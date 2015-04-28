def simple(c):
  if c in "ÁÉÍÓÚÜáéíóúüñÑ!¡¿?":
    if c in "Áá":return "A"
    if c in "Éé":return "E"
    if c in "Íí":return "I"
    if c in "Óó":return "O"
    if c in "ÚÜúü":return "U"
    if c in "Ññ":return "Ñ"
    if c in "!¡?¿":return "!"
  return c

def espalindromo(cad):
  c=""
  r=""
  for i in cad:
    if i.upper() in "AáÁBCDEÉéFGHIÍíJKLMNÑñOÓóPQRSTUÜúüÚVWXYZ!¡¿?":      
      r=simple(i)+r  
      c=c+simple(i)
  #print c.upper(),r.upper()
  return c.upper()==r.upper()

cad=raw_input("Dame una cadena: ")

if espalindromo(cad):
  print "La cadena es un palindromo"
else:
  print "La cadena no es un palindromo"