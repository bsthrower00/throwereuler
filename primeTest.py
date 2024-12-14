#prime test
from functools import reduce
import time
start = time.time()


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
    if len(factors) == 2:
        return True
    else:
        return False
    
    
    
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
        

count = 0
for i in range(1,1_000_000):
    if primeFacs(i):
        count += 1
        

print(count)



                    
end = time.time()
print("The time of execution of above program is :", end-start)                    
        