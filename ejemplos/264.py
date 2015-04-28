#farenheit a centigrados

def acentigrados(f):  
  return (f-32.0)*5.0/9.0

f=float(raw_input("Introduzca una cantidad de °F: "))

print "°C=",acentigrados(f)

  