#Programa que muestra todos los numeros potencia de 2 entre 20 y 230

listo=False
vamax=230
vamin=20
x=1
while listo==False:
  if (2**x>=vamin):
    if (2**x<=vamax):
      print 2**x      
    else:
      listo=True
  x+=1
