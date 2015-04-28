#lee cinco numeros y dice, de los cuatro ultimos cual esta
# mas cerca del primer numero introducido 

def distancia(x,y):
  return abs(abs(y)-abs(x))


primero=int(raw_input("Introduzca un numero: "))
proximo=0
for i in range(4):
  num=int(raw_input("Introduzca un numero: "))
  if i==0:proximo=num
  if distancia(primero,num)<distancia(primero,proximo):
    proximo=num

print "El numero mas cercano al primero (%d) es: %d"%(primero,proximo)
