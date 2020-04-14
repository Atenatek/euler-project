#Special Pythagorean triplet
   
#Problem 9

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2

#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import time
start_time = time.time()


def pythagorean_triplet(sum):
    # return a pythagorean triplet (a, b, c when a**2 + b**2 == c**2)
    # for witch a + b + c == sum
    # ex : pythagorean_triplet(12) return 3, 4, 5 
    
    for a in range(1, sum//3):
        for b in range(a, sum//2):
            for c in range(b, sum//2):
                if a**2 + b**2 == c**2 and (a + b + c) == sum:
                    print(a, b, c)

pythagorean_triplet(1000)


print("--- %s seconds ---" % (time.time() - start_time))
