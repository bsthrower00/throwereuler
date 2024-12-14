# #eu021 sums of amicable numbers
from functools import reduce
def SumOfFactors(n):
        step = 2 if n%2 else 1
        facSet = list(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(n**.5)+1, step) if n % i == 0)))
        facSet.pop(1)
        return sum(facSet)
 
# print(SumOfFactors(1))

 
# def ammicablePair(a,b):
    # if SumOfFactors(a) == b and SumOfFactors(b) == a:
        # return True
    # else:
        # return False

# # print(ammicablePair(220,284))


# ammicablePairSet = []       
# for i in range(1,10000):
    # for p in range(1,10000):
        # if p != i and ammicablePair(i,p) is True:
            # print(i,p)
            # ammicablePairSet.append(i)
# print(ammicablePairSet, sum(ammicablePairSet))          #[1, 6, 28, 220, 284, 496, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368, 8128] 40285


from math import ceil

# def d(n):
        # f = 0
        # for i in range (1,int(ceil(n/2)+1)):
                # if n%i == 0:
                        # f+=i
        # return f
# print(d(1))
summ = 0
for a in range(1,10000):
        b = SumOfFactors(a)
        if a == SumOfFactors(b) and a != b:
                summ += a

print(summ)