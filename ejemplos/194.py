#sustituye todas las vocales de una cadena por puntos

def sustituir(cadena):
  res= ""
  for i in cadena:
    if i in "AEIOUaeiouáéíóúüÁÉÍÓÚÜ":
      res+="."
    else:
      res+=i
  return res

cad = raw_input("Dame una cadena: ")

print sustituir(cad)

