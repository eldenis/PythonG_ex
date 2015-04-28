#Un programa que desglose una cantidad entera de euros
#en billetes de 500,200,100,50,20,10,5 y monedas de 1 y 2
#usando ciclos for-in

n=0
#input de n
while (n<=0):
  n=int(raw_input("Introduzca una cantidad entera de euros: "))

#declaracion de Denominaciones
billetes=[500,200,100,50,20,10,5]
monedas=[2,1]

print "\nBilletes"
print   "--------"

for i in billetes:
  if int(n/i)>0:
    print i,"¤  =",int(n/i)
    n=n-((int(n/i))*i)

if n>0:
  print "\n\nMonedas"
  print     "-------"
  for i in monedas:
    if int(n/i)>0:
      print i,"¤  =",int(n/i)
      n=n-((int(n/i))*i)