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
