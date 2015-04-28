#Un programa que lee una cadena y un k y dice si hay palabras
#con esa longitud hay en la cadena introducida

palabras=raw_input("Introduzca una cadena: ").split()
k=int(raw_input("Introduzca un numero: "))
hay=False
for palabra in palabras:
  if len(palabra)==k:
    hay=True
    break

if hay:
  print "Existen palabras con %d caracteres."% (k)
else:
  print "NO Existen palabras con %d caracteres."% (k)