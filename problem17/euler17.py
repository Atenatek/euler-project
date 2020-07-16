# Number letter counts
# Problem 17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


numbers = {
    1:'one', 
    2:'two', 
    3:'three', 
    4:'four', 
    5:'five', 
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    100:'hundred',
    }

#create a list of written numbers from 1 to 19
to_99 = [numbers[r] for r in range(1, 20)] 

#append 20 to 99 to the list
for d in range(20, 100, 10):
    to_99.append(f'{numbers[d]}')
    for u in range(1, 10):
        to_99.append(f'{numbers[d]} {numbers[u]}')

#create a list from 100 to 999
hundred_to_1000 = []
for u in range(1, 10):
    hundred_to_1000.append(f'{numbers[u]} {numbers[100]}')
    for n in to_99 :
        hundred_to_1000.append(f'{numbers[u]} {numbers[100]} and {n}')

#append 1000 to the list
hundred_to_1000.append('one thousand')

#join the 2 lists, creating a list from 1 to 1000
to_1000 = to_99 + hundred_to_1000

#add the len of each number of the list, removing the white spaces
n = 0
for num in to_1000 :
    n += len(num.replace(' ', ''))

print(n)