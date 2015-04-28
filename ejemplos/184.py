def esbinario(cad):
  if cad=="": return False
  for i in cad:
    if i not in "01":
      return False
  return True

while True:
  bits = raw_input('Dame un numero binario: ')
  if esbinario(bits):
    break
  else:
    print "Numero binario mal formado"

n = len(bits)
valor = 0
for bit in bits:
  if bit == '1':
    valor = valor + 2 ** (n-1)
  n -= 1

print 'Su valor decimal es', valor