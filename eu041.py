#pandigital prime
# numSet = set([1,2,3,4,5,6,7,8,9])
def checkPan(n):
    numSet = set([])
    for i in range(len(str(n))):
        numSet.add(i+1)
    s,l = '',[]
    i = 1
    while len(s) < len(numSet):
        s += str(n * i)
        i += 1
    for letter in s:
        l.append(int(letter))
    # print(numSet,l)
    if set(l).intersection(numSet) == numSet and len(l) == len(numSet):
        return True
    else:
        return False
        
from functools import reduce
def prime(n):
    if n == 0 or n == 1:
        return False
    step = 2 if n%2 else 1
    facSet = list(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**.5)+1, step) if n % i == 0)))
    # facSet.pop(1)
    # print(facSet)
    if len(facSet) == 2:
        return True
    else:
        return False
largest = 2143
for i in range(7_000_001,8_000_000,2):
    if prime(i) is True and checkPan(i) is True:
        largest = i
        print(i)
print(largest)        


# print(checkPan(654321))