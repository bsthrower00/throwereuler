#quadratic primes
from functools import reduce
def isPrime(n):
    step = 2 if n%2 else 1
    facSet = set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**.5)+1, step) if n % i == 0)))
    if len(facSet) == 2:
        return True
    else:
        return False

def tryPoly(a,b):
    check = False
    n = 0
    while check is False and n**2 + a*n+b > 0:
        # print(n,n**2 + a*n+b)
        if isPrime(n**2 + a*n+b) is True:
            n += 1
        else:
            check = True
    return n
most = [0, None, None]
for i in range(-1000,1000):
    for p in range(-1000,1000):
        if tryPoly(i,p) > most[0]:
            most = [tryPoly(i,p),i,p]
            print(most)
print(most)
            