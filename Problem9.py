# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^ + b^ = c^
# For example, 3^ + 4^ = 9 + 16 = 25 = 5^.
# There exist exactly one Pythagorean triplet for which a+b+c = 1000
# Find the product abc

for a in range(1, 998):
    for b in range(2,998):
        if a<b:
            c=1000-a-b
            if a**2+b**2==c**2:
                print("Liczby to: ", a, b, c, ", a ich produkt: ", a*b*c)