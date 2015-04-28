def esBisiesto(anio):
  return (anio%4==0 and anio%100!=0 or anio%400==0)

anio=int(raw_input("Introduzca un anio: "))

if esBisiesto(anio):
  print "El anio",anio,"es bisiesto"
else:
  print "El anio",anio,"NO es bisiesto"