def si_o_no(pregunta):
  respuesta=""
  opciones=["si","s","Si","SI","no","n","No","NO"]
  while respuesta not in opciones:
    respuesta=raw_input(pregunta)
    if respuesta not in opciones:
      print "OPCION INCORRECTA!\nLas opciones permitidas son:"
      print " ".join(opciones),"\n"
  return "S" in respuesta.upper()

r=si_o_no("Desea ingresar algun dato?: ")
print "Respuesta:",r