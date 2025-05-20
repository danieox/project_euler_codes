#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=55

def palindrome(num):
    new_num = num
    rem  = 0
    while(new_num>0):
            m = new_num%10
            rem = rem*10 + m
            new_num = new_num//10

    return num == rem

def palindrome_sum(n, iter = 50):
    orig = n
    for _ in range(iter):
        a = str(orig)
        b = ''
        for j in range(len(a) - 1, -1, -1):
            b += a[j] 
        reverse_num = int(b)  
        total = orig + reverse_num
        if palindrome(total):
            return True
        orig = total
    return False
    
lychrel = []
for i in range(10000):
    if not palindrome_sum(i):
        lychrel.append(i)

print(len(lychrel))




        
