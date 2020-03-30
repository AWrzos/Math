# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# liczba 2 ma indeks 1
indeks=2
liczba=3
spis={1:2}
while indeks <= 10001:
    pierwsza=True
    for dzielnik in range(2,liczba):
        if liczba % dzielnik == 0:
            pierwsza=False
            pass
    if pierwsza==True:
        spis[indeks]=liczba
        indeks+=1
    liczba+=1
print(spis[10001])

