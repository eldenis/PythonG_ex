def eshex(cad):
  if cad=="": return False
  for i in cad.upper():
    if i not in "0123456789ABCDEF":
      return False
  return True

def hexadec(cad):
  cad=cad.upper()
  res=0 
  dighex="0123456789ABCDEF"
  for i in cad:
    if i !="0":
      d=dighex.find(i)
      res=16*res+d
      
  return res

while True:
  num = raw_input('Dame un numero en hexadecimal: ')
  if eshex(num):
    break
  else:
    print "Numero hex mal formado"

print "Su valor decimal es", hexadec(num)
