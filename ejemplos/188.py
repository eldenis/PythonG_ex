def decaoct(numdec):
  cont=len(str(numdec))
  res=0
  tmp=""
  while (numdec>0):
    res=int(numdec/(8**cont))
    tmp+=str(res)
    numdec-=(8**cont)*res
    cont-=1
  return tmp

num = int(raw_input('Dame un numero: '))
print "Su valor octal es", decaoct(num)
