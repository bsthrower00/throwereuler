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


def findNthPrime(p):
    listOfPrimes = [2]
    walk = 3
    while len(listOfPrimes) < p:
        if isPrime(walk) is True:
            listOfPrimes.append(walk)
        walk += 2 
    return (listOfPrimes[p-1])

def whichPrime():
    q = int(input('Which number prime do you want to find? (enter an integer): '))
    print(findNthPrime(q))

whichPrime()