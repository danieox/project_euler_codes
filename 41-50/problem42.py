#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=42

with open('C:/Users/user/Downloads/euler/words.txt') as f: # use own path
    words = f.read().replace('"', '').split(',')
max_length = max([len(w) for w in words])

alpha_numerical = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
    'Z': 26}

triangle_number = []
for n in range(1,26*max_length):
    T = 0.5*n*(n+1)
    triangle_number.append(T)

triangle_word = []
for a in words:
    total = sum(alpha_numerical[i] for i in a)
    if total in triangle_number:
        triangle_word.append(a)

print(len(triangle_word))
    







