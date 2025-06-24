#! /usr/bin/python3

# link to problem: https://projecteuler.net/problem=49

def prime_check(n):
    if n < 2: 
        return False
    for p in range(2, int(n**0.5)+1):
        if n % p == 0:
            return False
    return True


prime_perms = []

for i in range(1000,10000):
    for j in range(i+1,10000):
        k = 2*j - i
        if k >= 10000:
            continue
        if prime_check(i) and prime_check(j) and prime_check(k):
            if sorted(str(i)) == sorted(str(j)) == sorted(str(k)):
                prime_perms.append((i, j, k))

print(prime_perms)

for s in prime_perms:
    new_str = ''
    for num in s:
        new_str += str(num)
    print(new_str)
