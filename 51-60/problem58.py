#! /usr/bin/python

# link to problems: https://projecteuler.net/problem=58

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

diagonals = [1]
spiral_numbers = 1
limit = 2
spiral_prime = []

while True:
    for _ in range(4):
        spiral_numbers += limit
        diagonals.append(spiral_numbers)
        if is_prime(spiral_numbers):
            spiral_prime.append(spiral_numbers)

    if (len(spiral_prime)/len(diagonals)) * 100 < 10:
        print(limit+1)
        break
    limit += 2
