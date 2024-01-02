# fmt: off
from math import sqrt


def prime_factors(n):
    primes = set()

    while n % 2:
        primes.add(2)
        n //= 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        while not n % i:
            primes.add(i)
            n //= i

    if n != 1: primes.add(n)
    return primes

def phi(n):
    primes = prime_factors(n)


    return int(res)

    
while (n := int(input())) != 0:
    primes = set()

    while n % 2:
        primes.add(2)
        n //= 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        while not n % i:
            primes.add(i)
            n //= i

    if n != 1: primes.add(n)

    res = n
    for p in primes:
        res *= (1-1/p)
    print(n)
