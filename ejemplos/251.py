
m = int(raw_input('Dime el numero de filas: '))
n = int(raw_input('Dime el numero de columnas: '))


A = []
for i in range(m):
  A.append( [0] * n )

print 'Lectura de la matriz A'
for i in range(m):
  for j in range(n):
    A[i][j] = float(raw_input('Dame el componente (%d,%d): ' % (i, j)))


num=int(raw_input("Introduzca un numero para multiplicar la matriz: "))

B = []
for i in range(m):
  B.append( [0] * n )

# Empieza el calculo del producto .
for i in range(m):
  for j in range(n):
    B[i][j] = A[i][j] *num


print "Producto:"
for i in range(m):
  for j in range(n):
    print B[i][j],
  print