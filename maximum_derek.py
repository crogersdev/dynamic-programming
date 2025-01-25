#!/usr/bin/env python3

def maximum_derek(vals, n):
    # Base case: When only one value remains, return it
    if n == 1:
        return vals[0]

    # Recursive case: Consider the last two elements
    max_result = float('-inf')  # Start with the smallest possible number

    for op in ['+', '-', '*', '/']:
        if op == '+':
            result = vals[n-2] + vals[n-1]
        elif op == '-':
            result = vals[n-2] - vals[n-1]
        elif op == '*':
            result = vals[n-2] * vals[n-1]
        elif op == '/' and vals[n-1] != 0:  # Guard against division by zero
            result = vals[n-2] / vals[n-1]
        else:
            continue  # Skip invalid operations

        # Create a new list with the operation result replacing the last two elements
        new_vals = vals[:n-2] + [result]
        max_result = max(max_result, maximum_derek(new_vals, n-1))

    return max_result


if __name__ == '__main__':
    values = [-2, 0, 1, -2]

    print(maximum_derek(values, len(values)))