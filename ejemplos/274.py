#Con solo llegar hasta n/2 es suficiente
def es_perfecto(n):
  sumatorio = 0
  for i in range(1, (n/2)+1):
    if n % i == 0:
      sumatorio += i
  return sumatorio == n

print es_perfecto(28)