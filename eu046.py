#goldbachs other conjecture
from functools import reduce
squares = reduce(list.__add__,([n**2] for n in range(1,1000)))
# print(squares)
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
primes = reduce(list.__add__,([n] for n in range(1,10_000) if prime(n)))


# print(primes[:6])
for n in range(4141,100_000,2):
    if prime(n) is False:
        check = False
        for p in primes:
            if p<n and check is False:
                for s in squares: 
                    if (p + 2 * s) <= n:
                        if (p + 2 * s) == n:
                            print(n,p,s)
                            check = True
                            break
        if check is False:
            print(n,' cant be expressed')
            break

# a = True
# while a is True:
    # for i in range(10):
        # print('hi',i)
        # if i == 7:
            # a = False
            # break