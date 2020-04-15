#Summation of primes
   
#Problem 10

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

import time
start_time = time.time()

def is_prime(n):
    # return True if a num is prime number
    # otherwise return False
    # num type : int
    
    if n <= 1:
        return False
    elif n == 2:
        return True
    i = 3
    while (i * i <= n):
        if n % i == 0:
            return False
        i += 2
    return True

def summary_of_prime(x):
    # return the sum of prime number below x

    res = 2
    for x in range(3, x , 2):
        if is_prime(x):
            res += x
    return res

print(summary_of_prime(2000000))

print("--- %s seconds ---" % (time.time() - start_time))