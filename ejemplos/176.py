"""
Escribir un programa que lea una cadena por teclado
y diga si la cadena forma un identificador de variable
valido
"""

def valido(cad):
  reservadas=["and","assert","break","class","continue","def",\
  "del","elif","else","except","exec","finally","for","from",\
  "global","if","import","in","is","lambda","not","or","pass","print"\
  "raise","return","try","while","yield"]
  chars="_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  digitos="0123456789"
  if cad=="": return False
  if cad[0].upper() not in chars:#no empieza con caracter
    return False  
  elif " " in cad:#tiene espacios
    return False
  elif cad.lower() in reservadas: return False #Es una palabra reservada
  else:    
    for i in cad:
      if (i.upper() not in chars) and (i not in digitos):#tiene caracteres que no son digitos o letras
        return False
  return True



cad=raw_input("Introduzca una cadena: ")

if valido(cad):
  print "La cadena es un identificador valido."
else:
  print "La cadena NO es un identificador."
