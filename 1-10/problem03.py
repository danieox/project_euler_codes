#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=3

import math
def largest_factor(n):
    while n % 2 == 0:
        max_prime = 2
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            max_prime = i
            n //= i
        i += 2

    if n > 2:
        max_prime = n

    return max_prime

# print(largest_factor(13195))
print(largest_factor(600851475143))
