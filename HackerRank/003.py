#!/bin/python3

import sys, math

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

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_factor(n))
