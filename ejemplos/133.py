from math import sqrt

num = int(raw_input("Dame un numero: "))
creo_que_es_primo = True

for divisor in range(2, int(num/2)):
  if num % divisor == 0:
    creo_que_es_primo = False
    break

if creo_que_es_primo:
  print "El numero", num, "es primo"
else:
  print "El numero", num, "no es primo"
