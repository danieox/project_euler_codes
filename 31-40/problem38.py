#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=38

pandigital = ['1','2','3','4','5','6','7','8','9']
large_pandigital = 0

for a in range(9,10000):
    n = 1
    b = ''
    while len(b) < len(pandigital):
        b += str(a*n)
        n += 1
        if len(b) == len(pandigital) and sorted(b) == pandigitaland int(b) > large_pandigital:
            large_pandigital = int(b)
          
print(large_pandigital)


