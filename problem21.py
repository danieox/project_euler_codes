#! /usr/bin/python

# Let d(𝑛) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n). 
# If d(a) = b and d(b) = a, where 𝑎 ≠ 𝑏, then a and 𝑏 are an amicable pair, and each of a and b are called amicable numbers. 
# For example, the proper divisors of 220 are: 1,2,4,5,10,11,20,22,44,55,110; therefore d(220)=284. The proper divisors of 284 are: 1,2,4,71,142; so d(284)=220. 
# Evaluate the sum of all the amicable numbers under 10000.

def sum_of_proper_div(num):
    divisor = []
    for d in range(1,num):
        if num % d == 0:
            divisor.append(d)
    sum_one = 0
    for i in range(len(divisor)):
        sum_one += divisor[i]
    return(sum_one)


def amicable(m):
    pairs = []
    for a in range(2,m):
        y = sum_of_proper_div(a)
        if y != a: 
            p = sum_of_proper_div(y)
            if p == a:
                if ((a,y) and (y,a)) not in pairs:
                    pairs.append((a,y))
                  
    sum_two = 0
    for j in pairs:
        for k in (0,1):
            sum_two += j[k]
    return sum_two

print(amicable(10000))
