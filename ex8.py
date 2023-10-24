def sequencia1(x):
  if x == 1:
    return x
  else:

    return sequencia1(x - 1) * 3


numero_sequencia = int(input("Digite um numero: "))

print(sequencia1(numero_sequencia))


def sequencia2(x):
  if x == 1:
    return x * 2

  else:
    return sequencia2(x - 1) / 2


numero_sequencia2 = int(input("Digite um numero: "))

print(sequencia2(numero_sequencia2))


def sequencia3(x, a, b):
  if x == 1:
    return a
  elif x == 2:
    return b
  elif x <= 0:
    return 0

  else:
    return sequencia3(x - 1, a, b) + sequencia3(x - 2, a, b)


a = int(input("Digite um valor pra A: "))

b = int(input("Digite um valor pra B: "))

numero_sequencia3 = int(input("Digite um numero: "))

print(sequencia3(numero_sequencia3, a, b))


def sequencia4(n, p, q):
  if n == 1:
    return p
  elif n % 2 == 0:
    return sequencia4(n - 1, p, q) - (n // 2) * q
  else:
    return sequencia4(n - 1, p, q) + ((n + 1) // 2) * q


p = 10
q = 3
n = 7

resultado = sequencia4(n, p, q)

print(f'S({n}) = {resultado}')
