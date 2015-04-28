#Construir una matriz identidad de nxn

n=int(raw_input("Introduzca un entero que indica el\n"\
"tamaño de la matriz: "))

matrizid=[]
for i in range(n):
  matrizid.append([0]*n)

for i in range(0,len(matrizid)):
  for j in range(0,len(matrizid[i])):
    if i==j: matrizid[i][j]=1

for i in matrizid:
  print i