#!/usr/bin/env python3

'''
this one doesn't work out to be a good candidate for recursion
i'm guessing because you don't get to recurse over
substructures of exactly the same ... well, structure

given values   = [1, 3, 0]
use tabulation = [1, 1, 1]

each position in tabulation indicates the longest increasing subsequence
which ends at that index

you can nest two for loops to continue to evaluate up to that point
selecting the maximum between 1 + tab[i] and tab[j] provided
i > j
and
values[i] > values[j]

and you bump tab[i] because it goes up if it's part of a subsequence
and you know it's part of subsequence if those two conditions hold
because the previous value will be less than the current

but previous != the one right before current, it just means
"definitely before the current one"

'''

if __name__ == '__main__':
    values = [1, 0, 3, 2, -1, 5, 7]
    N = len(values)
    tab = [1] * N

    # we're going to start at 1 because a values array of length 1 
    # would cause us to return "1" with no computation necessary
    for i in range(1, N):
        for j in range(i):
            if values[i] > values[j]:
                # remember, we bump tab[j] and not tab[i] because
                # tab[j] is part of tab[i]'s sequence
                tab[i] = max(1+tab[j], tab[i])

    print(f"lis of {values}\nis {max(tab)}")
