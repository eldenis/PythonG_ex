#suma cada una de las columnas de una matriz
#y crea un vector con la sumatoria


m = int(raw_input('Dime el numero de filas: '))
n = int(raw_input('Dime el numero de columnas: '))

A = []
for i in range(m):
  A.append( [0] * n )

print 'Lectura de la matriz A'
for i in range(m):
  for j in range(n):
    A[i][j] = int(raw_input('Dame el componente (%d,%d): ' % (i, j)))

V=[0]*n

for i in range(n):
  for j in range(m):
    V[i]+=A[j][i]

print "\n\nMatriz:"
for i in A:print i
print "\n\nV:",V