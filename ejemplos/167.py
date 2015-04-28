#Un programa que lee una cadena y un k y dice cuantas palabras
#con esa longitud hay en la cadena introducida

palabras=raw_input("Introduzca una cadena: ").split()
k=int(raw_input("Introduzca un numero: "))
cont=0
for palabra in palabras:
  if len(palabra)==k:
    cont+=1

print "Existen %d palabras con %d caracteres."% (cont,k)