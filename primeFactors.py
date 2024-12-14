# determine largest prime factor of 600851475143 

def primeFactors(num):
    for i in range(2,int(num ** .5)+1):
        if num % i == 0:
            print(i)
            primeFactors(i)
primeFactors(600851475143)            