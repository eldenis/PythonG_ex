#matriz diagonal superior: todos los elementos
#por debajo de la diagonal principal son 0

def matrizds(matriz):
  for i in range(m):
    for j in range(n):
      if j<i and matriz[i][j]>0:
        return False
  return True


m = int(raw_input('Dime el numero de filas: '))
n = int(raw_input('Dime el numero de columnas: '))

A = []
for i in range(m):
  A.append( [0] * n )

print 'Lectura de la matriz A'
for i in range(m):
  for j in range(n):
    A[i][j] = float(raw_input('Dame el componente (%d,%d): ' % (i, j)))

if matrizds(A):
  print "La matriz es diagonal superior"
else:
  print "La matriz no es diagonal superior"