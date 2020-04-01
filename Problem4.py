# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

liczba2 = 0
liczba = 0
palindrom = []
for i in range(100, 1000):
    for j in range(100, 1000):
        liczba = i * j
        liczba = str(liczba)
        liczba2 = liczba[::-1]
        if liczba == liczba2:
            liczba = int(liczba)
            palindrom.append(liczba)
        liczba = 0
        liczba2 = 0
print(palindrom)
print("wynik: ", max(palindrom))
