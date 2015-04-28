#Un programa que lee una cadena y un k y dice si todas las palabras
#tienen esa longitud hay en la cadena introducida

palabras=raw_input("Introduzca una cadena: ").split()
k=int(raw_input("Introduzca un numero: "))
todas=True
for palabra in palabras:
  if len(palabra)!=k:
    todas=False
    break

if todas:
  print "Todas las palabras tienen %d caracteres."% (k)
else:
  print "NO todas las palabras tienen %d caracteres."% (k)