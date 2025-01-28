#!/usr/bin/env python3

def permute(path, remaining):
    if not remaining:
        res.append(path[:])
        return
    
    for i in range(len(remaining)):
        permute(path + [remaining[i]], remaining[:i] + remaining[i+1:])


vals = ['a', 'b', 'c']

N = len(vals)
res, sol = [], []

permute(list[int](), vals)

print(f"{res}")
