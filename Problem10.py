import math

# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
suma = 2
liczba = 3
while liczba < 2000000:
    pierwsza = True
    for dzielnik in range(2, math.ceil(math.sqrt(liczba)) + 1):
        if liczba % dzielnik == 0:
            pierwsza = False
            pass
    if pierwsza == True:
        suma += liczba
        print(liczba)
    liczba += 2
print("Ostateczna suma:", suma)
