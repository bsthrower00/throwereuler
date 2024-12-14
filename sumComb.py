#sum combos
# A Python program to print all
# combinations of given length
from itertools import combinations
l = [4,5,6,7,8,9]

#
def SC(s, n, targ):
    ss = set([])
    s = [ item for item in s for repetitions in range(n) ]
    print(s)
    for i in list(combinations(s,n)):
        if sum(i) == targ:
            ss.add(i)
    for p in ss:
        if 8 in p:
            print(p)

SC(l, 4,25)