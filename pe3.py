result = 600851475143
primo = 1

while(result!=1):
    primo += 1
    while(result%primo==0):
        result /= primo

print(primo)