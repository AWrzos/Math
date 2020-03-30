# Sum square difference
# problem
# The sum of the squares of the first ten natural numbers is 1^+2^+...+10^=385
# The square of the sum of the first ten natural numbers is (1+2+...+10)^=55^=3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sk=0 #suma kwadratów
ks=0 #kwadrat sumy
for i in range(1,101):
    sk+=i**2
    ks+=i

print("Kwadrat sumy: ", ks**2)
print("Suma kwadratów: ", sk)

print("Odpowiedź, czyli różnica dwóch powyższych wartości: ", ks**2 - sk)
