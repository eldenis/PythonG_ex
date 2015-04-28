#lee una cadena y agrega todas sus palabras a una lista sin repetir palabras

def existeEnLista(p):
  for i in lista:
    if p==i:
      return True
  return False

cadena= raw_input("Introduzca una cadena: ")

lista=[]

for palabra in cadena.split():
  if not existeEnLista(palabra):
    lista.append(palabra)
    
print lista