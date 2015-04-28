def fueraRango(numero):
  if numero in range(11):return False
  return True

n=-1
while (fueraRango(n)):
  n=int(raw_input("Introduzca un numero entre 0 y 10 (ambos inclusive): "))
