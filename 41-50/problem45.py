#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=45 
import math

def roots(a,b,c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    sqrt_d = math.sqrt(discriminant)
    return (-b + sqrt_d) / (2*a)

n = 286
while True:
    T = (n * n + n) // 2
    P = roots(3, -1, -2 * T)
    H = roots(2, -1, -1 * T)

    if P is not None and H is not None and P.is_integer() and H.is_integer():
        print(T)
        break
    n+=1
    

