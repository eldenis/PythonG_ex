def simple(c):
  if c in "��������������!��?":
    if c in "��":return "A"
    if c in "��":return "E"
    if c in "��":return "I"
    if c in "��":return "O"
    if c in "����":return "U"
    if c in "��":return "�"
    if c in "!�?�":return "!"
  return c

def espalindromo(cad):
  c=""
  r=""
  for i in cad:
    if i.upper() in "A��BCDE��FGHI��JKLMN��O��PQRSTU����VWXYZ!��?":      
      r=simple(i)+r  
      c=c+simple(i)
  #print c.upper(),r.upper()
  return c.upper()==r.upper()

cad=raw_input("Dame una cadena: ")

if espalindromo(cad):
  print "La cadena es un palindromo"
else:
  print "La cadena no es un palindromo"