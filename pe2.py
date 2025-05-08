#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

atual = 2
anterior = 1
troca = 0
soma = 0

while (atual < 4000000):

    if (atual % 2) == 0:
        soma = soma + atual

    troca = atual
    atual = atual + anterior
    anterior = troca

print(soma)