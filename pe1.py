#Find the sum of all the multiples of 3 or 5 below 100.

soma = 0 

for i in range (1000):
    if (i % 3 == 0) or (i % 5 == 0):
        soma = soma + i

print(soma)