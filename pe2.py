atual = 2
anterior = 1
troca = 0
soma = 0

while (atual < 4,000,000):

    if (atual % 2) == 0:
        soma = soma + atual

    troca = atual
    atual = atual + anterior
    anterior = troca

print(soma)