#Largest palindrome product
   
#Problem 4

#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

palindromes = []
for a in range(999,99,-1):
    for b in range(999,99,-1):
        if str(a * b)[0] == str(a * b)[-1] and str(a * b)[1] == str(a * b)[-2] and str(a * b)[2] == str(a * b)[-3]:
            palindromes.append(a * b)

print(max(palindromes))