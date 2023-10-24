def calcular_P(n):
  if n == 1:
      return 1
  else:
      return n**2 * calcular_P(n - 1) + n - 1

n = int(input("Digite o valor de n: "))
resultado = calcular_P(n)
print(f"O valor de P({n}) é {resultado}")
