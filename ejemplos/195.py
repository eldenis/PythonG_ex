#Mostrar la extensión de un nombre de archivo
def ext(nom):
  i= nom.find(".")
  if i==-1:
    return ""
  else:
    return nom[i+1:len(nom)]


nom=raw_input("Introduzca un nombre de archivo: ")

e=ext(nom)
if e=="":
  print "La extensión es vacia"
else:
  print "Su extensión es:",e
