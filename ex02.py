# P(1) = a
# P(n) = r * P(n - 1), para n > 1

def progressao_geometrica(a, r, n):
  if n == 1:
      return a
  else:
      return r * progressao_geometrica(a, r, n - 1)

termo_inicial = float(input("Digite o termo inicial (a): "))
razao = float(input("Digite a razão (r): "))
n_termos = int(input("Digite o número de termos (n): "))

for n in range(1, n_termos + 1):
  resultado = progressao_geometrica(termo_inicial, razao, n)
  print(f"P({n}) = {resultado}")

