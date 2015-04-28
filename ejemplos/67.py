#leer euros, una tasa de interes, y un numero de anos
#y decir en cuanto se habra convertido el capital inicial 
#transcurridos esos anos si cada ano se aplica a la de interes
#introducida. CconInteres=c*(1+(x/100))**n

c=float(raw_input("Introduzca el capital: "))
x=float(raw_input("Introduzca el interes: "))
n=int(raw_input("Introduzca la cantidad de anos: "))

if x>0:
  res=c*((1+(x/100))**n)
  print "%f a %d anos con un interes de %f es %f"%(c,n,x,res)
else:
  print "x no es una cantidad positiva"