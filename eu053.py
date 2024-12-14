#Combinatoric selections
from math import factorial 
def comb(n,r):
    return (factorial(n)/((factorial(r)*(factorial(n-r)))))

ge = 0
for i in range(101):
    for p in range(101):
        if p<i and comb(i,p) > 1_000_000:
            ge += 1
print(ge)            