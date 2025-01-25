### fibonacci
the 'hello world' of dynamic programming
don't forget to use memoization

### knapsack 0/1
given an array of length N of item weights and an associated array of item values, and a knapsack of weight capacity M such that total weight is under capacity and maximum value put in the knapsack
relies on the intuition that at each item's consideration you have two choices: keep or don't keep
keep means adding the value and lowering capacity
dont keep means doing nothing
both considerations move you through the array
since the similarity of each consideration is just the current item and the state of the knapsack
it's an easy day to recurse through the array starting at the end and going backwards and at each choice decide to keep or not keep
the recursive call comes from the considerations of keeping vs not keeping and you select the max between the two

### longest increasing subsequence
given an array of integers find the longest subsequence -- not sub array, so subsequence is not contiguous -- going from left to right
i kept trying to shoehorn a recursive approach onto this but it didn't work because there's no way to consider the same structure in recursive calls, you have to keep iterating through the array and considering everything before you.  so, doubly nested for loop it is.
use tabulation
initalize your tabulation as an array of length(values) and set each tabulation[i] = 1 because at the very start you can safely assume that the minimum length any spot in the array will have will be 1
then, iterate through your array and consider the previous values
if values[i] > values[j]
and you make sure i > j
then you can bump evaluate a max between 1+tabulation[j] (because it'll be part of the increasing sequence as it's less than the values[i] you're currently at) and tabulation[i]'s current value
then you set tabulation[i] to be the max between the two
