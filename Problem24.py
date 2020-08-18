import math

# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#
# Solution

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
result = ""
perm = 9
sum = 0

while perm > 0:
    fact = math.factorial(perm)
    i = len(digits) - 1
    do = True
    while do == True:
        if sum + (fact * i) < 1000000:
            sum += (fact * i)
            result += digits[i]
            digits.remove(digits[i])
            do = False
        i -= 1
    perm -= 1

result += digits[0]

print(result)
