# A)

def numero_de_bacterias(n):
    if n == 0:
        return 50000
    else:
        return 3 * numero_de_bacterias(n - 1)

n = int(input("Digite o valor de n:"))
bacterias_iniciais = numero_de_bacterias(n)
print(f"População de bactérias no {n}º período de tempo: {bacterias_iniciais}")

# B) a população exederá 200.000 quando N = 2, onde n = 2 resulta em 450.000 bactérias