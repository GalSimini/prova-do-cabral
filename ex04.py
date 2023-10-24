# Uma coleção M de números é definida recursivamente por:
# 2  M e 3  M
# Se X  M e Y  M, então X*Y  M .
# Quais dos seguintes números pertencem a M? 6 , 9 , 16 , 21 , 26 , 54 , 72 , 218.
# Faça um programa recursivo para demonstrar. (0,25)

M = [2, 3]
NumbersToCheck = [6, 9, 16, 21, 26, 54, 72, 218]

encontrado = []
naoencontrado = []

print(M)


def check_colecao(x, y):
  new = x * y
  if new > 300:
    return
  else:
    if x in M and y in M:
      M.append((new))
      check_colecao(x, new)
      check_colecao(y, new)
      check_colecao(new, new)


check_colecao(2, 3)
check_colecao(2, 2)
check_colecao(3, 3)
print(M)

for n in NumbersToCheck:
  if n in M:
    encontrado.append(n)
  else:
    naoencontrado.append(n)

print(f"Encontrado: {encontrado}")
print(f"Não Encontrado: {naoencontrado}")
