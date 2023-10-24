def calcular_D(n):
  if n == 1:
      return 3
  elif n == 2:
      return 5
  else:
      return (n - 1) * calcular_D(n - 1) + (n - 2) * calcular_D(n - 2)

n = int(input("Digite o valor de n: "))
resultado = calcular_D(n)
print(f"O valor de D({n}) é {resultado}")
