#truncatable primes
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
  
#lis = reduce(list.__add__,([-1 * i] for i in range(10)))  
     
primeList = []
for i in range(11,1000000,2):#1,1_000_01,2):
    a =[]
    if prime(i) is True:
        l = list(set(reduce(list.__add__,([int(str(i)[:p+1]),int(str(i)[p:])] for p in range(len(str(i)))))))
        for item in l:
            a.append(prime(item))
        if all(a) is True:
            primeList.append(i)
print(primeList,'sum is: ',sum(primeList))
        
    
