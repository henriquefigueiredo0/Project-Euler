#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

numero = 0
achou = 0

while (achou == 0):

    numero = numero + 1

    for i in range (1,21):
        if (numero % i) != 0:
            break
        if i == 20:
            achou = 1

print(numero)


