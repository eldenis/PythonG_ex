#Mostrar la extensi�n de un nombre de archivo
def ext(nom):
  i= nom.find(".")
  if i==-1:
    return ""
  else:
    return nom[i+1:len(nom)]


nom=raw_input("Introduzca un nombre de archivo: ")

e=ext(nom)
if e=="":
  print "La extensi�n es vacia"
else:
  print "Su extensi�n es:",e
