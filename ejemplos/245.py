#Construir una matriz identidad de 4x4


matrizid=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(0,len(matrizid)):
  for j in range(0,len(matrizid[i])):
    if i==j: matrizid[i][j]=1

for i in matrizid:
  print i