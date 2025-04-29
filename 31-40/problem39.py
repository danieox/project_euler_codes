#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=39
import time

start_time = time.time()
Right_triangles = []
Counter = []
Perimeter = []

for p in range(1, 1001):
    count = 0
    for a in range(1, p//2):
        for b in range(a,(p-a)//2):
            c = p - a - b
            if p == a+b+c and c*c == a*a + b*b:
                triple = tuple(sorted((a, b, c)))
                if triple not in [t[:3] for t in Right_triangles]:
                    Right_triangles.append((triple[0], triple[1], triple[2], p))
                    count += 1
    Counter.append(count)
    Perimeter.append(p)

max_count = 0
index = 0
for i in range(len(Counter)):
    if Counter[i] > max_count:
        max_count = Counter[i]
        index = Perimeter[i]

print(max_count, index)
run_time = time.time() - start_time
print(run_time)
