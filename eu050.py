#consecutive prime sum
from functools import reduce

with open('primes.txt','r') as f:
    l = f.readline()
    primeList = l.split(',')
    for i in range(len(primeList)-1):
        primeList[i] = int(primeList[i])
            
    def prime(n):
        if n <= 0 or n == 1:
            return False
        step = 2 if n%2 else 1
        facSet = list(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(n**.5)+1, step) if n % i == 0)))
        if len(facSet) == 2:
            return True
        else:
            return False    
        
    highest = [0,0,0]      
    for i in range(len(primeList)-1):
        print(i,' u are gay')
        for j in range(len(primeList)-1):
            s = sum(primeList[i:j])
            if s > 1_000_000:
                break
            # print(i,j,s)
            if i<j and s%2 == 1 and s in primeList and s <1_000_000:
                if j-i > highest[0]:
                    highest = [j-i,sum(primeList[i:j]),i]
                    print(highest)
    print('highest is', highest)