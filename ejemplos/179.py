def esbinario(cad):
  if cad=="": return False
  for i in cad:
    if i not in "01":
      return False
  return True

while True:
  cad=raw_input("Introduzca un numero binario: ")
  if esbinario(cad):
    break
  else:
    print "La cadena no representa un numero binario"
  

