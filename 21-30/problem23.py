#! /usr/bin/python

# link to question: https://projecteuler.net/problem=23

# function for finding perfect, deficient and abundant numbers
def abundant_numbers(num):
    perfect = []
    deficient = []
    abundant = []
    
    for i in range(1,num):
        total = 0
        for j in range(1,i):
            if i%j == 0:
                total += j 
            else:
                total += 0
        if total == i:
            perfect.append(i)
        elif total < i:
            deficient.append(i)
        elif total > i:
            abundant.append(i)

# finding the non-abundant sums
    abundant_set = set(abundant)  
    digit = []
    for k in range(1, num):
        can_be_written = False
        for a in abundant:
            if a > k:
                break
            if (k - a) in abundant_set:
                can_be_written = True
                break
        if not can_be_written:
            digit.append(k)

    res = sum(digit)
    return abundant[0:20], digit[0:20], res

print(abundant_numbers(28123))

## takes about 120 seconds to compute


