#Smallest multiple
   
#Problem 5

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

def is_prime(n):
    i = 2
    while (i * i <= n):
        if n % i == 0:
            return False
        i = i + 1
    return True

def divisible_by_all(result, value):

    for n in range(2, value + 1):
        if result % n != 0:
            return False
    return True


def try_to_divide(value):

    res = 1
    for x in range(2, value + 1):
        if is_prime(x):
            res = res * x
    while divisible_by_all(res, value) == False:
        res += 1
    else:
        print(res)

try_to_divide(20)