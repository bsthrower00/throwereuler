# sum of primes

def isPrime(n):
    if n == 2: 
        return True
    elif n>1:
        for i in range(2,int(n ** .5)+1):
            if (n%i)==0:
                return False
        return True
    else:
        return False 


def sumPrimes(p):
    listOfPrimes = [2]
    walk = 3
    while walk < p:
        if isPrime(walk) is True:
            listOfPrimes.append(walk)
        walk += 2 
    print(sum(listOfPrimes))
sumPrimes(2000000)