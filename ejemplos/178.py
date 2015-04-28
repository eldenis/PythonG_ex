def bienparentesis(cad):
  abren=0
  cierran=0
  for i in cad:
    if i=="(":
      abren+=1
    elif i==")":
      cierran+=1
  return abren==cierran
  
cad =raw_input("Introduzca una cadena: ")
if bienparentesis(cad):
  print "La cadena esta bien parentizada."
else:
  print "La cadena esta mal parentizada."