# 2^15 = 32768
# and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

liczba=2**1000
liczba=str(liczba)
suma=0
for i in range(0, len(liczba)):
    n=liczba[i]
    n=int(n)
    suma+=n
print(suma)