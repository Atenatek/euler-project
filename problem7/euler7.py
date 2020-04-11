# 10001st prime
   
# Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11,
# and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
  
def is_prime(n):
    # return True if a num is prime number
    # otherwise return False
    # num type : int
    
    if n <= 1:
        return False
    i = 2
    while (i * i <= n):
        if n % i == 0:
            return False
        i = i + 1
    return True

def count_prime(index):
    # count_prime(6) return 13, the 6th prime number
    # input and ouput type : int
    
    count = 1
    num = 3
    while count <= index:
        if is_prime(num):
            count +=1
            if count == index:
                break
        num +=2
    return num

print(count_prime(10001))