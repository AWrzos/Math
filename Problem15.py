# Starting in the top left corner of a 2×2 grid,
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
n=40
k=n/2
k=int(k)
nsilnia=1
for i in range(1,n+1):
    nsilnia*=i
nksilnia=1
for i in range(1,n-k+1):
    nksilnia*=i
ksilnia=1
for i in range(1,k+1):
    ksilnia*=i
wynik=nsilnia/(ksilnia*nksilnia)
print(wynik)