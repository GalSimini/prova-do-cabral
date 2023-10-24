def pertence_a_T(numero):
  if numero == 2:
      return True
  elif numero < 2:
      return False
  else:
      return (pertence_a_T(numero - 3) or pertence_a_T(numero / 2))

numeros = [6, 7, 19, 12]

for numero in numeros:
  if pertence_a_T(numero):
      print(f'{numero} pertence a T')
  else:
      print(f'{numero} não pertence a T')
