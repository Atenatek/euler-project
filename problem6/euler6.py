#Sum square difference
   
#Problem 6

#The sum of the squares of the first ten natural numbers is,
#1**2+2**2+...+10**2=385

#The square of the sum of the first ten natural numbers is,
#(1+2+...+10)**2=55**2=3025

#Hence the difference between the sum of the squares of the first
#ten natural numbers and the square of the sum is 3025−385=2640

#Find the difference between the sum of the squares of the 
#first one hundred natural numbers and the square of the sum.

def square_sum(num):
    #return the sum of the squares of nat numbers from 1 to num
    #ex : square_sum(3) return sum(1**2+2**2+3**2) = 14
    #input & output type : int
    sq_list = []
    for n in range(1, num + 1):
        sq_list.append(n**2)
    return sum(sq_list)

def sum_square(num):
    #return the square of the sums of nat numbers from 1 to num
    #ex : sum_square(3) return (1+2+3)**2 = 36
    #input & output type : int
    res = 0
    for n in range(1, num + 1):
        res += n
    return(res**2)

def dif_sqsum_sumsq(num):
    #return the difference between sum_square and square_sum
    #ex : dif_sqsum_sumsq(n3) return 36 - 14 = 22
    #input & output type : int
    return (sum_square(num) - square_sum(num))

print(dif_sqsum_sumsq(10))
print(dif_sqsum_sumsq(100))