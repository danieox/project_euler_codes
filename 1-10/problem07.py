#! /usr/bin/python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

primes = [2, 3, 5]
p = 6

while len(primes) < 10002:
    if all(p%q != 0 for q in primes if q*q <= p):
            primes.append(p)

    p = p+1

s = primes[10001 - 1]
print("The 10001st prime is " + str(s))
