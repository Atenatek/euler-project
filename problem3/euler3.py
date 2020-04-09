#Largest prime factor  
#Problem 3

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


def isprime(num):
    # return True if a num is prime number
    # otherwise return False
    # num type : int
    
    for i in range(2, int(num//2)):
        if (num % i) == 0:
            print(str(i) + ' est un diviseur')
            break
        else:
            print(str(i) + ' est premier')


isprime(10)

def factors(num):
    #return a list of factors of num
    # ex : factors(12) = [1, 2, 3, 4, 6]
    f = []
    for i in range(1, num):
        if num % i == 0:
            f.append(i)
    return f
