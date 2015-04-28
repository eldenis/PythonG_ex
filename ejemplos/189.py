#Leer un numero octal y mostrarlo en binario

def octadec(cad):
  res=0
  cont=len(cad)-1
  for i in cad:
    if i !="0":
      res+=int(i)*(8**cont)
    cont-=1
  return res


def decabin(numdec):
  tmp=""
  while (numdec>0):
    tmp= str(numdec%2)+tmp
    numdec=numdec/2
  return tmp

oct=raw_input("Dame un numero en octal: ")
print "Su representacion binaria es:",decabin(octadec(oct))

