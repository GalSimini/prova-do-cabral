def calcular_W(n):
  if n == 1:
      return 2
  elif n == 2:
      return 5
  else:
      return calcular_W(n - 1) * calcular_W(n - 2)

n = int(input("Digite o valor de n: "))
resultado = calcular_W(n)
print(f"O valor de W({n}) é {resultado}")
