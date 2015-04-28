#prefijo comun de los elemenos de una lista


def sacarprefijo(lista):
  pmc= buscarpalabramascorta(lista)
  c=0
  pref=""
  for i in pmc.upper():    
    for j in lista:
      if i!=j[c].upper(): return pref
    pref+=i
    c+=1  
  return pref

def buscarpalabramascorta(lista):
  res=lista[0]
  for i in lista:
    if len(res)>len(i):
      res=i
  return res

n=int(raw_input("Introduzca el tamano de la lista: "))
V=[0]*n
for i in range(n):
  V[i]=raw_input("Introduzca posicion %d de la lista: "%(i+1))
  
print sacarprefijo(V)