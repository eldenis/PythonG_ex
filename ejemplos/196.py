def sumabinaria(a,b):
  res=""
  if len(a)>len(b):
    b=b.zfill(len(a))
  elif len(b)>len(a):
    a=a.zfill(len(b))          
  acarreo="0"
  for i in range(len(a)-1,-1,-1):
    if acarreo=="0":
      if a[i]=="1" and b[i]=="1" :tmp="0";acarreo="1"
      if a[i]=="1" and b[i]=="0" :tmp="1"
      if a[i]=="0" and b[i]=="1" :tmp="1"
      if a[i]=="0" and b[i]=="0" :tmp="0"
    else:
      if a[i]=="1" and b[i]=="1" :tmp="1";
      if a[i]=="1" and b[i]=="0" :tmp="0";
      if a[i]=="0" and b[i]=="1" :tmp="0";
      if a[i]=="0" and b[i]=="0" :tmp="1";acarreo="0"         

    res= tmp +res

  if acarreo=="1": res="1"+res
  return res



a=raw_input("Introduzca un numero binario: ")
b=raw_input("Introduzca un numero binario: ")

print "El resultado de la sumatoria es:",sumabinaria(a,b)

