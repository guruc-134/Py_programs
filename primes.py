import math

def primeFactors(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            n = n / i
    if n > 2:
        primes.append(n)
    return primes

i = int(input())

print(primeFactors(i))
