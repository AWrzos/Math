# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
from fractions import Fraction

result_d=0
length_d=0
d=983
while d<1000:
    k = str(d)
    nominator = 10 ** len(k)
    i=1
    before=0
    list_r=[]
    length=""
    while True:
        r=nominator/d
        r=str(r)
        r=int(r[0])
        m=nominator%d
        if r in list_r:
            break
        if m!=0:
            if before=True:
                list_r.append(r)
            nominator=m*10
        else:
            break
    length=len(list_r)
    if length>length_d:
        length_d=length
        result_d=d
    d+=1
print("wynik: ", result_d, "długość: ", length_d)

