def transformar(n):
  if n<5:
    return "Suspenso"
  if n>=5 and n<7:
    return "Aprobado"
  if n>=7 and n<8.5:
    return "Notable"
  if n>=8.5 and n<10:
    return "Sobresaliente"      
  if n==10:
    return "Matricula de honor"
  else: 
    return "Error: La nota maxima es 10"
  

nota=float(raw_input("Introduzca la nota: "))

print "La nota cualitativa es <<%s>>"%transformar(nota)