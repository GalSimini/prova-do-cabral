def calcular_B(n):
  if n == 1:
      return 1
  else:
      return calcular_B(n - 1) + n**2

n = int(input("Digite o valor de n: "))
resultado = calcular_B(n)
print(f"O valor de B({n}) é {resultado}")
