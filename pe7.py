def eh_primo(num):
    for i in range(2, int((num/2)+1)):
        if (num%i==0):
            return 0
    return 1

numero = 2
indice = 0

while(True):
    if eh_primo(numero):
        indice += 1
    if (indice == 10001):
        break
    numero += 1

print(numero)
