#factortest
from functools import reduce
print("prime factors this:" + str(n:= int(input("please enter positive whole number"))) + str(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**.5)+1, 2 if n%2 else 1 ) if n % i == 0)))))

 