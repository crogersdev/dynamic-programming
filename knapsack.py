#!/usr/bin/env python3

def knapsack(capacity: int, n: int) -> int:
    # if there are no items to add then we get a knapsack value of 0 
    # OR
    # if our backpack has no room we get a value of 0
    if n == 0 or capacity == 0:
        return 0

    # do we even have room for it?  if not, don't keep it and move on
    if capacity < weights[n-1]:
        return knapsack(capacity, n-1)

    # have we seen this before, or do we have to compute it?  if so, let's use it from the memo
    if (capacity, weights[n-1]) in memo:
        return memo[(capacity, n-1)]

    # we have room for it but let's see if it's optimal to add
    keep = values[n-1] + knapsack(capacity-weights[n-1], n-1)
    dont_keep = knapsack(capacity, n-1)
    max_val = max(keep, dont_keep)
    memo[(capacity, n-1)] = max_val
    return max_val


if __name__ == "__main__":
    values = [10, 80, 11, 12]
    weights = [4, 3, 1, 3]
    capacity = 5

    memo = {}

    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50 

    print(f"given weights {weights}\nof values {values}\nand a knapsack of capacity {capacity}")
    print(f"our knapsack can hold an optimized value of {knapsack(capacity, len(weights))}")