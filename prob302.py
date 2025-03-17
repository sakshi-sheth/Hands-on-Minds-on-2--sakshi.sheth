from sympy import factorint, isprime
from math import isqrt, gcd
from functools import lru_cache

@lru_cache(None)
def is_perfect_power(n):
    # To Check if n is a perfect power
    for base in range(2, isqrt(n) + 1):
        power = 2
        while (p := base ** power) <= n:
            if p == n:
                return True
            power += 1
    return False

@lru_cache(None)
def is_powerful(n):
    #To Check if n is powerful
    factors = factorint(n)
    return all(exp >= 2 for exp in factors.values())

@lru_cache(None)
def is_achilles(n):
    return is_powerful(n) and not is_perfect_power(n)

@lru_cache(None)
def phi(n):
    result = n
    for p in factorint(n):
        result *= (1 - 1/p)
    return int(result)

def count_strong_achilles(limit):
    count = 0
    for n in range(2, limit):
        if is_achilles(n):
            if is_achilles(phi(n)):
                count += 1
    return count

# a small test for output
print("Count of Strong Achilles numbers below 10^6:", count_strong_achilles(10**6))
