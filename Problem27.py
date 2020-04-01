import math
# Quadratic primes
# Problem 27
# Pelna tresc w pliku Problem27.jpg
# Find the product of the coefficients, a and b,
# for the quadratic expression that produces the maximum number of primes
# for consecutive values of n, starting with n=0.
liczba = 0
ilosc2 = 0
wynika = 0
wynikb = 0
ilosc = 0
for a in range(-999, 1000):
    for b in range(2, 1001):
        ilosc = 0
        pierwsza = True
        n = 0
        while True:
            liczba = n ** 2 + a * n + b
            if liczba>0:
                for dzielnik in range(2, math.ceil(liczba / 2 + 1)):
                    if liczba % dzielnik == 0:
                        pierwsza = False
                        break
                if pierwsza == False:
                    break
                else:
                    ilosc += 1
                    n += 1
            else:
                break
        if ilosc > ilosc2:
            ilosc2 = ilosc
            wynika = a
            wynikb = b

print("a:", wynika, "b:", wynikb, ", tworzą liczb pierwszych: ", ilosc2)
print("Iloczyn a i b: ", wynika * wynikb)
