#119 raiz n-esima de un numero n
numero = float(raw_input('Dame un numero: '))

for n in range(2, 101):
  print 'la raiz %d-esima de %4.2f es %f' % (n, numero, numero**(1.0/n))