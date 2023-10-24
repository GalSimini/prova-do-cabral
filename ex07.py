def binarias_com_zeros_impares(n):
  if n == 0:
      return [""]
  if n == 1:
      return ["0", "1"]

  com_zeros_pares = ["0" + s for s in binarias_com_zeros_impares(n - 1)]
  com_zeros_impares = ["1" + s for s in binarias_com_zeros_impares(n - 1)]

  return com_zeros_pares + com_zeros_impares

n = int(input("Digite um número inteiro (n): "))

if n % 2 == 0:
  print("O número de zeros deve ser ímpar para gerar as cadeias corretas.")
else:
  resultado = binarias_com_zeros_impares(n)
  print(f"Cadeias binárias com um número ímpar de zeros (para n = {n}):")
  for cadeia in resultado:
      print(cadeia)