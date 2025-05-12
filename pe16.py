pot = 1
soma = 0
indice = 0

for i in range (0,1000):
    pot *= 2

nome = str(pot)
print(nome)

for i in nome:
    soma += int(nome[indice])
    indice += 1

print(soma)