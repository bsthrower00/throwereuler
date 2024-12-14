#distince prime factors
from functools import reduce
import time
start = time.time()
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

def primeFacss(n):
    if n == 0 or n == 1:
        return False
    step = 2 if n%2 else 1
    facSet = list(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**.5)+1, step) if n % i == 0)))
    new = []
    for item in facSet:
        if prime(item) and item not in new:
            new.append(item)
    return len(new)
    

def primeFacs(n):
    factors = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return len(factors)
    
    
    
check=True    
for i in range(100000,1000000):
    if check == False:
        break
    elif primeFacs(i) == 4:
        if primeFacs(i+1) == 4:
            if primeFacs(i+2) == 4:
                if primeFacs(i+3) == 4:
                    print(i)
                    check = False
                    
                    
end = time.time()
print("The time of execution of above program is :", end-start)                    
