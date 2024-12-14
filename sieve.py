#sieve
def sieve(n):
    arr = [True]*n
    for i in range(2,int(n**.5)+1):
        if arr[i] is True:
            for j in range(i**2,n,i):
                arr[j] = False
    
    return arr

a = sieve(699_000_000)
primeList = []
for i in range(len(a)):
    if a[i] is True:
        primeList.append(i)
with open('primes699.txt','w+') as f:
    
        f.write(str(primeList))
print('done')