"""Longest Collatz sequence
   
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

note: Once the chain starts the terms are allowed to go above one million.
"""

import time

start_time = time.time()

def transform(n):
    # n type : int
    # if n is even, return n/2
    # if n is odd, return 3n + 1
    # return type : int
    if n < 1:
        raise Exception("Sorry, no numbers below 1") 
    elif n % 2 == 0:
        return int(n/2)
    else:
        return 3 * n + 1

def collatz(n):
    # return the sequence of Collatz Problem as a list, starting from n
    seq = [n]                       # first item of the sequence is n
    res = n                         # first instance of transform result is n
    while res > 1:
        seq.append(transform(res))  # append to sequence the transformed number
        res = transform(res)    
    return seq

def longest_chain(r):
    # return the starting number of the longest collatz chain in range r
    # return the lenght of this chain
    res = 0
    max_n = r
    for n in range(r, 0, -1):
        if len(collatz(n)) > res:
            res = len(collatz(n))
            max_n = n
        else:
            continue
    return max_n, res

print(longest_chain(999999))

print("Proceeded in %s seconds" %(time.time() - start_time))


