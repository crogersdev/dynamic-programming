#!/usr/bin/env python3

def backtrack(i: int) -> None:
    if i == N:
        res.append(sol[:])
        return
    
    backtrack(i+1)
    
    sol.append(values[i])
    backtrack(i+1)
    sol.pop()

values = ['a', 'b', 'c']
N = len(values)

res, sol = [], []
backtrack(0)
print(res)