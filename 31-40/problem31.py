#! /usr/bin/python
import time

start_time = time.time()
def coin_sum(target):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (target + 1)
    ways[0] = 1 

    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]
    return ways[target]


print(coin_sum(200))
run_time = time.time() - start_time
print(f"runtime: {run_time}")

