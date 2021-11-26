import time

# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
# #
# # 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# # It is possible to make £2 in the following way:
# #
# # 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# # How many different ways can £2 be made using any number of coins?

# Solution

# # A   B   C   D    E    F    G              H
# # 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# # _   _   _    _    _    _    _              _   -8different coins
# # 200 100 40   20  10   4     2              1 - maximum
# scheme:
# # max 2 pounds, if 200 stop
# # after x times max -= 1
possibleways=200*100*40*20*10*4*2

counter = 1 # 1x£2


t=time.time()
sum=0
for G in range(0,2+1):
    for F in range(0,4+1):
        for E in range(0,10+1):
            for D in range(0,20+1):
                for C in range(0,40+1):
                    for B in range(0,100+1):
                        for A in range(0,200+1):
                            sum=G * 100 + F * 50 + E * 20 + D * 10 + C * 5 + B * 2 + A
                            if sum==200:
                                counter+=1
                                print(G,F,E,D,C,B,A,counter)
time=time.time()-t
print(counter, ", czas: ", time)

# 73682 , czas:  3465.274468421936
