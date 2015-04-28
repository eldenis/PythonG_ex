def octadec(cad):
  res=0
  cont=len(cad)-1
  for i in cad:
    if i !="0":
      res+=int(i)*(8**cont)
    cont-=1
  return res

def hexadec(cad):
  cad=cad.upper()
  res=0 
  dighex="0123456789ABCDEF"
  for i in cad:
    if i !="0":
      d=dighex.find(i)
      res=16*res+d      
  return res

def convertir(cad):
  if cad=="": return 0
  if cad.upper().startswith("0X"): return hexadec(cad[2:len(cad)])
  if cad.startswith("0"): return octadec(cad)
  for i in cad:
    if i not in "0123456789":
      return -1
  return int(cad)


num=raw_input("Introduzca un valor oct(ej. 0127), hex(ej. 0xFF), dec(ej 127): ")
c=convertir(num)

if c==-1:
  print "El numero tiene un formato erroneo"
else:
  print num,"=",c
