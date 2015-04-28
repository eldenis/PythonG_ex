#Un programa que lee una cadena y un k y dice si todas las palabras son largas
#Sino dice hay algunas cortas
#palabras largas son palabras len(palabra)>=k

palabras=raw_input("Introduzca una cadena: ").split()
k=int(raw_input("Introduzca un numero: "))
todaslargas=True
for palabra in palabras:
  if len(palabra)<k:
    todaslargas=False
    break

if todaslargas:
  print "Todas las palabras son largas"
else:
  print "Hay alguna palabra corta"