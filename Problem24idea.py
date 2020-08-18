# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#
# Solution


# 0 _ _ _ _ _ _ _ _ _
#   9*8*7*6*5*4*3*2*1 combinations
sum=(9*8*7*6*5*4*3*2)*2 #725760
print("Liczba kombinacji z 0 i 1 z przodu: ", sum)
# Millionth lexicographic permutation starts with 2
# 2 _ _ _ _ _ _ _ _ _
#(left: 013 456 789)

sum+=(8*7*6*5*4*3*2)*6 #967680
#  took (6+1)th number and put it in second position
# 2 7 _ _ _ _ _ _ _ _
#(left: 013 456 89)

sum+=(7*6*5*4*3*2)*6 #997920
# 2 7 8 _ _ _ _ _ _ _
#(left: 013 456 9)

sum+=(6*5*4*3*2)*2 #999360
# 2 7 8 3 _ _ _ _ _ _
#(left: 014 569)

sum+=(5*4*3*2)*5 #999960
# 2 7 8 3 9 _ _ _ _ _
#(left: 014 56)

sum+=(4*3*2) #999984
# 2 7 8 3 9 1 _ _ _ _
#(left: 0456)

sum+=(3*2)*2 #999996
# 2 7 8 3 9 1 5 _ _ _
#(left: 046)

sum+=(2) #999998
# 2 7 8 3 9 1 5 4 _ _
#(left: 06)

sum+=(2) #1000000

# 2 7 8 3 9 1 3 4 6 _
#(left: 0)

# 2 7 8 3 9 1 3 4 6 0