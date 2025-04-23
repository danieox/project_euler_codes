#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=12

def int_sqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def count_divisors(n):
    count = 0
    sqrt_n = int_sqrt(n)
    for k in range(1, sqrt_n + 1):
        if n % k == 0:
            count += 2 if k != n // k else 1
    return count

A = []
for a in range(1,1000000):
    A.append(a)


num = 0
B = []
for i in range(len(A)):
    num += A[i] 
    B.append(num)


C = []
maxi = 500
answer = 0

for j in range(len(B)):
    temp = count_divisors(B[j])
    C.append(temp)
    if temp > maxi:
        answer = B[j]
        break


print("First 10 integers:", A[:10])
print("First 10 triangle numbers:", B[:10])
print("First 10 divisor counts:", C[:10])
print("First triangle number with more than 500 divisors: ", answer)
