def Rotina(L, j):
  if j == 1:
      return L

  max_index = L.index(max(L[:j])) 
  
  L[max_index], L[j - 1] = L[j - 1], L[max_index] 

  return Rotina(L, j - 1)


L = [3, 7, 4, 2, 6]


resultado = Rotina(L, 5)

print("Lista resultante:", resultado)
print("Total de chamadas realizadas:", 5)
