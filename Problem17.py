# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens.
# For example, 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.
liczby1=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
liczby2=["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
liczby22=["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
liczba2="hundred"
liczba3="onethousand"
suma=0
#1-19
for cyfra in liczby1:
    suma+=len(cyfra)

wynik=100*suma

for liczba in liczby2:
    suma+=len(liczba)

#20-99
for liczba in liczby22:
    suma += len(liczba)
    for cyfra in liczby1:
        suma += len(cyfra)
        suma += len(liczba)

wynik+=(suma*9)
wynik+=len("hundredand")*999
wynik+=len("hundred")*9
wynik+=len(liczba3)
print("Wynik: ",wynik)