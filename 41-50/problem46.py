#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=46
def generate_prime(num):
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



goldbach = []
non_goldbach = []
n = 9
while n < 10**4:
    if n % 2 == 1 and n not in generate_prime(n+1):  
        comp_odd = False
        prime_set = generate_prime(n)
        for a in prime_set:
            for j in range(1,int(((n - a) / 2)**0.5) + 1):
                if n == a + 2 * j**2:
                    goldbach.append(n)
                    comp_odd = True
                    break
            if comp_odd:
                break
        if not comp_odd:
            non_goldbach.append(n)
    n += 2

print(min(non_goldbach))       
