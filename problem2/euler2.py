#Even Fibonacci numbers
   
#Problem 2

#Each new term in the Fibonacci sequence is generated 
# by adding the previous two terms. By starting with 
# 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci
# sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

def fibo(n):
    #return a list af the fibonnacci serie, up to n
    a = 0
    b = 1
    fibolist = []
    while b < n:
        c = a + b
        a = b
        b = c
        fibolist.append(a)
    return fibolist


def even(l):
    # return a a list wih only even numbers of the input
    # l type : list
    # return type : list
    # ex : even([3, 4, 5, 6, 7, 8]) = [4, 6, 8]

    evenlist = []
    for num in l:
        if num % 2 == 0:
            evenlist.append(num)
        else:
            continue
    return evenlist

# print the sum of the even numbers of fibo(4000000)
print(sum(even(fibo(4000000))))