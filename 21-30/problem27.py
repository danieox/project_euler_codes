import math

def prime_check(n):
    if n < 2: 
        return False
    for p in range(2, int(n**0.5)+1):
        if n % p == 0:
            return False
    return True


count = 0
best_a = 0
best_b = 0

for a in range(-999,1000):
    for b in range(-1000,1001):
        n = 0
        while True: 
            c = n*n + a*n + b
            if prime_check(c):
                n += 1
            else:
                break
        if n > count:
            count = n
            best_a = a
            best_b = b
            
print(best_a * best_b)
