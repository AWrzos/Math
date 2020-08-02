# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

# Solution
suma = 0
n = 2
while n < 10001:
    dzielniki = 0
    for i in range(1, int((n / 2) + 2)):
        if n % i == 0:
            dzielniki += i
    dzielnikipary = 0
    for j in range(1, int(dzielniki / 2 + 2)):
        if dzielniki % j == 0:
            dzielnikipary += j
    if n != dzielniki and n == dzielnikipary:
        suma+=n
    n += 1

print("Wynik: ", suma)
