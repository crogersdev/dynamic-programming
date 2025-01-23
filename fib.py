#!/usr/bin/env python3

memo = {}

def fib(n: int) -> int:
    if n == 1:
        return 0 
    if n == 0:
        return 1

    if n in memo:
        return memo[n]

    ans = fib(n-1) + fib(n-2)
    memo[n] = ans
    
    return ans

if __name__ == '__main__':
    # 0: 0
    # 1: 1)
    print("doing fibonacci")
    print(fib(500))