limite = int(raw_input('Introduzca cuantos numeros primos quiere: '))

primos = [0]*limite

i=0
num=1
while i<limite:
  num+=1
  creo_que_es_primo = True
  for divisor in range(2, num):
    if num % divisor == 0:
      creo_que_es_primo = False
      break
  if creo_que_es_primo:
    primos[i]=num
    i+=1

print primos