#prime pair sets
with open('primes.txt','r') as f:
    l = f.readline()
    primeList = l.split(',')
    for i in range(len(primeList)-1):
        primeList[i] = int(primeList[i])
        
      