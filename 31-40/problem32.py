#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=32
import time

start_time = time.time()
digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
temp = []

for a in range(1,10000):
    for b in range(1,1000):
        c = a * b
        d = list(str(a) + str(b) + str(c))
        if sorted(d) == digit:
            temp.append(c)

pandigital = []
for i in range(len(temp)):
    if temp[i] not in pandigital:
        pandigital.append(temp[i])        
            
print(sum(pandigital))
run_time = time.time() - start_time
print(run_time)
