def calcular_A(n):
  if n == 1:
      return 2
  else:
      return calcular_A(n - 1) - 1

n = int(input("Digite o valor de n: "))
resultado = calcular_A(n)
print(f"O valor de A({n}) é {resultado}")
