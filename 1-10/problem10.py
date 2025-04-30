#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=10

import math

def is_prime(num):
    primes = []
    for n in range(2, num):
        is_prime = True
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes

print(sum(is_prime(2*(10**6))))
