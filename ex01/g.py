def calcular_T(n):
  if n == 1:
      return 1
  elif n == 2:
      return 2
  elif n == 3:
      return 3
  else:
      return calcular_T(n - 1) + 2 * calcular_T(n - 2) + 3 * calcular_T(n - 3)

n = int(input("Digite o valor de n: "))
resultado = calcular_T(n)
print(f"O valor de T({n}) é {resultado}")
