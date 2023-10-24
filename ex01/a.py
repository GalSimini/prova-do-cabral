def calcular_S(n):
  if n == 1:
      return 10
  else:
      return calcular_S(n - 1) + 10

n = int(input("Digite o valor de n: "))
resultado = calcular_S(n)
print(f"O valor de S({n}) é {resultado}")

