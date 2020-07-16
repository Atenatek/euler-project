
# Problem 16
# Power digit sum
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def pwr_dig_sum(x):
    pwr = 2**x
    sum = 0
    for d in str(pwr):
        sum += int(d)
    return sum

print(pwr_dig_sum(1000))