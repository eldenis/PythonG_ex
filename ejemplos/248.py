#Construir una matriz identidad de 4x4

matrizid=[]
for i in range(4):
  matrizid.append([0]*4)

for i in range(0,len(matrizid)):
  for j in range(0,len(matrizid[i])):
    if i==j: matrizid[i][j]=1

for i in matrizid:
  print i