#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=25

f1 = 1
f2 = 1
index = 2

while True:
    fn = f1 + f2
    f1 = f2
    f2 = fn
    index += 1
    
    if len(str(fn)) == 1000:
        break

print(index)
