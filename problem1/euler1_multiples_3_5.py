#Project Euler.net

#Multiples of 3 and 5

#Problem 1

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def multiples(r, *n):
    #Function returns a list of multiples of numbers in a given range.
    # r : range
    # *n : multiples
    # type *n, r : int
    # return a list of the multiples of *n in range(r)
    #     example : multiples(10, 3, 5) return [3, 5, 6, 9]

    l = []
    for x in range(r):
        for num in n:
            if x % num == 0 and x not in l:
                l.append(x)
            else:
                continue
    return l

print(sum(multiples(1000, 3, 5)))