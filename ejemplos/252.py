#Matriz transpuesta
m = int(raw_input('Dime el numero de filas: '))
n = int(raw_input('Dime el numero de columnas: '))


A = []
for i in range(m):
  A.append( [0] * n )

print 'Lectura de la matriz A'
for i in range(m):
  for j in range(n):
    A[i][j] = int(raw_input('Dame el componente (%d,%d): ' % (i, j)))


At = []
for i in range(n):
  At.append( [0] * m )


for i in range(n):
  for j in range(m):
    At[i][j] = A[j][i] 


print "\nMatriz normal:"
for i in range(m):
  for j in range(n):
    print A[i][j],
  print

print "\nMatriz transpuesta:"
for i in range(n):
  for j in range(m):
    print At[i][j],
  print