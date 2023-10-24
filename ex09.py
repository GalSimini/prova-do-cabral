def triangulos(x):
  if x == 1:
    return x
  else:
    numero_adicional = x

    return numero_adicional + triangulos(x-1)


numero = int(input("Digite um numero: "))

print(triangulos(numero))