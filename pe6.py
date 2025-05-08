#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_sq = 0
sq_sum = 0

for i in range(101): # soma dos quadrados
    sum_sq = i ** 2 + sum_sq
    
for i in range(101): #quadrados da soma
    sq_sum = i + sq_sum
sq_sum = sq_sum ** 2

difference = sq_sum - sum_sq

print(difference)