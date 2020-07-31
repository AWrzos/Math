# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,April, June and November.
# All the rest have thirty-one,
# February twenty-eight, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# Solution
sundays=0
days=1 # days counter; if |7 => sunday
months=[31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year=1900

while year < 1901:
    days += 31
    if year % 4 == 0:
        days += 29
    else:
        days += 28
    for month in months:
        days += month
    year += 1

while year <2001:
    if days % 7 == 0: # january
        sundays+=1
    days += 31
    if days % 7 == 0: # february
        sundays+=1
    if year % 4 == 0:
        days+=29
    else:
        days+=28
    for month in months:
        if days % 7 == 0:
            sundays += 1
        days += month
    year+=1

print(sundays)

