#! /usr/bin/python

# link to question: https://projecteuler.net/problem=22
with open('C:/Users/user/Downloads/euler/names.txt') as f:
    names = f.read().replace('"', '').split(',')
sorted_names = sorted(names)


alpha_numerical = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
    'Z': 26}

result = 0
for name in sorted_names:
    total = sum(alpha_numerical[i] for i in name)
    prod = total * (sorted_names.index(name)+1)
    result += prod

print(result)
