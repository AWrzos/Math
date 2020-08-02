# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

# Solution
silnia=1
suma=0

for i in range(1,101):
    silnia*=i

silnianap=str(silnia)
for j in range(0, len(silnianap)):
    suma+=int(silnianap[j])

print("Silnia wynosi: ", silnia, ", zaś suma: ", suma)
