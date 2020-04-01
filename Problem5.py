# Definitywnie do poprawki

# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
liczba = 20
while True:
    if liczba % 20 == 0:  # 2, 4, 5, 10, 20
        if liczba % 19 == 0:  # 19
            if liczba % 18 == 0:  # 6, 9, 18
                if liczba % 17 == 0:  # 17
                    if liczba % 16 == 0:  # 8, 16
                        if liczba % 15 == 0:  # 3, 5, 15
                            if liczba % 14 == 0:  # 7, 14
                                if liczba % 13 == 0:  # 13
                                    if liczba % 12 == 0:
                                        if liczba % 11 == 0:
                                            print(liczba)
                                            break
    liczba += 2

# dla przykładowego rozwiązania
liczba = 12
while True:
    if liczba % 10 == 0:
        if liczba % 9 == 0:
            if liczba % 8 == 0:
                if liczba % 7 == 0:
                    print(liczba)
                    break

    liczba += 2
