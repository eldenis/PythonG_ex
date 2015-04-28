"""
Decir si una matriz es prima
Ej matriz prima:
  [  3 ,  5 ,  9 ]=17
  [  5 ,  9 ,  3 ]=17
  [  9 ,  3 ,  5 ]=17
  ----------------
    17   17   17
"""

def esprima(matriz):  
  suma=sum(matriz[0])
  for i in matriz:
    if sum(i)!=suma:return False
  
  for j in range(n):
    tmp=0
    for i in range(m):
      tmp+=matriz[i][j]
    if tmp!=suma:return False
  
  return True

m = int(raw_input('Dime el numero de filas: '))
n = int(raw_input('Dime el numero de columnas: '))

A = []
for i in range(m):
  A.append( [0] * n )

print 'Lectura de la matriz A'
for i in range(m):
  for j in range(n):
    A[i][j] = int(raw_input('Dame el componente (%d,%d): ' % (i, j)))
    
if esprima(A):
  print "La matriz es prima"
else:
  print "La matriz NO es prima"