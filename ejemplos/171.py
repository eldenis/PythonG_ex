#Un programa que lee una cadena y un k y dice si todas las palabras son cortas
#Sino dice hay algunas largas
#palabras largas son palabras len(palabra)>k

palabras=raw_input("Introduzca una cadena: ").split()
k=int(raw_input("Introduzca un numero: "))
todascortas=True
for palabra in palabras:
  if len(palabra)>k:
    todascortas=False
    break

if todascortas:
  print "Todas las palabras son cortas"
else:
  print "Hay alguna palabra larga"