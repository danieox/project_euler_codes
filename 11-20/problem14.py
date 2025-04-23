#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=14

maxi = 0

for i in range(2,1000000):
    count = 1
    num = i
    while(num > 1):
        if num%2 == 0:
            num = num//2 # even case
        else:
            num = 3*num + 1 # odd case
        count += 1
        continue
        
    if count > maxi:
        maxi = count
        start = i

print("Starting number: ", start)
