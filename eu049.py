#prime permutations
from functools import reduce
def prime(n):
    if n == 0 or n == 1:
        return False
    step = 2 if n%2 else 1
    facSet = list(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**.5)+1, step) if n % i == 0)))
    if len(facSet) == 2:
        return True
    else:
        return False    
        
        
        
def isPerm(a,b,c):
    a,b,c=str(a),str(b),str(c)
    setA=set()
    setB=set()
    setC=set()
    for i in range(4):
        setA.add(a[i])
        setB.add(b[i])
        setC.add(c[i])
    if setA == setB and setA == setC:
        return True
    else: return False

primeList = []
for i in range(1000,10000):
    if prime(i):
        primeList.append(i)
print(len(primeList))
for item in primeList:
    for i in range(1,4500):
        if item + 2*i < 9999:
            if prime(item+i) and prime(item + 2*i):
                if isPerm(item, item+i, item + 2*i):
                    print(str(item),str(item+i),str(item+2*i))