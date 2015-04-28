#Un programa que lee una cadena y un k y dice si hay palabras largas
#palabras largas son palabras len(palabra)>k

palabras=raw_input("Introduzca una cadena: ").split()
k=int(raw_input("Introduzca un numero: "))
haylargas=False
for palabra in palabras:
  if len(palabra)>k:
    haylargas=True
    break

if haylargas:
  print "Hay palabras largas"
else:
  print "No hay palabras largas"