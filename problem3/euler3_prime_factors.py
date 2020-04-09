#Largest prime factor  
#Problem 3

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

import math

def factors_under_sqrt(num):
    # return factors of a number between 2 and sqrt(num)
    # ex: factors_under_sqrt(100) return [2, 4, 5, 10]
    f = []
    for x in range(2,round(math.sqrt(num)) + 1):
        if num % x == 0:
            f.append(x)
    return f

def isprime(num):
    # return True if a num is prime number
    # otherwise return False
    # num type : int
    
    if (num==1):
        return False
    else:
        for x in range(2,num//2):
            if(num % x==0):
                return False
        return True

for x in factors_under_sqrt(600851475143):
    if isprime(x):
        print(x)