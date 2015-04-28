def menu(opciones):
  opcion = ''
  while len(opcion) !=1 or int(opcion)<1 or int(opcion)>len(opciones):
    print 'Menu de opciones'
    for i in range(len(opciones)):
      print i+1,"- ",opciones[i]

    opcion = raw_input('Escoja una opcion: ')
    if len(opcion)<1 or int(opcion)<1 or int(opcion)>len(opciones):
      print 'Opcion incorrecta, intente de nuevo.'
  return opcion

opcs=["Introducir datos","Consultar","Salir"]
o=menu(opcs)
print "Opcion elegida:",o