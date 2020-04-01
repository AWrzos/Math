# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
Liczba = 600851475143
dzielniki = []
while Liczba != 1:
    for i in range(2, Liczba + 1):
        if Liczba % i == 0 and i != 1:
            Liczba = int(Liczba / i)
            dzielniki.append(i)
            break
print("Dzielniki: ", dzielniki)
print("Największy z dzielników: ", max(dzielniki))
