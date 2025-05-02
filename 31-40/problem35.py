#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=35

import math

def prime_generator(num):
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
    
prime = (prime_generator(10**6))

circ_primes = []
for i in prime:
    a = str(i)
    is_circular = True
    for j in range(len(a)):
        b = int(a[j:] + a[:j]) 
        if b not in prime:
            is_circular = False
            break
    if is_circular:
        circ_primes.append(i)

print(len(circ_primes))


