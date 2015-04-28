#Programa que muestra todos los numeros potencia de 2 entre 20 y 230
#El operador & compara los bits que componen el valor de una variable
#en el caso que x=32 seria asi
#x   = 32=100000
#x-1 = 31=011111
#         ------
#res = 00=000000
#Al aplicar el operador &, se evalua verticalmente los valores
#y si son 1 y 1 el resultado es 1, de lo contrario el resultado seria 0
#El resultado del operador de bits and (&) seria = 0. Eso nos indica que
#el numero es potencia de dos.


for x in range(20,231): 
  if (x & (x-1))==0: print x


