def tieneMayus(texto):
  mayus="ABCDEFGHIJKLMN�OPQRSTUVWXYZ"
  for i in texto:
    if i in mayus:return True
  return False

introducido="TEXTO"
while (tieneMayus(introducido)):
  introducido=raw_input("Introduzca un texto sin mayusculas: ")
