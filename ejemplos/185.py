def esoctal(cad):
  if cad=="": return False
  for i in cad:
    if i not in "01234567":
      return False
  return True

def octadec(cad):
  res=0
  cont=len(cad)-1
  for i in cad:
    if i !="0":
      res+=int(i)*(8**cont)
    cont-=1
  return res

while True:
  num = raw_input('Dame un numero en octal: ')
  if esoctal(num):
    break
  else:
    print "Numero octal mal formado"

print "Su valor decimal es ", octadec(num)