def pertence_a_w(s):
  if len(s) == 0:
      return True  # A cadeia vazia pertence a W

  if s[0] == 'a' and s[-1] == 'c':
      inner = s[1:-1]  # Remover o primeiro 'a' e o último 'c'
      return pertence_a_w(inner)

  if s == 'bc':
      return True

  return False

# Testando as cadeias
cadeias = ["a(b)c", "a(a(b)c)c", "a(abc)c", "a(a(a(a)c)c)c", "a(aacc)c"]
for cadeia in cadeias:
  if pertence_a_w(cadeia):
      print(f"{cadeia} - pertence a W")
  else:
      print(f"{cadeia} - não pertence a W")
