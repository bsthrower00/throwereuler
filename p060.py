#prime pair sets
from itertools import combinations, permutations


with open('primes.txt','r') as f:
    l = f.readline().split(', ')
    # print(len(a))
    s = set(l)
    # print('5' in s)
    # print(l[0:5])
    
    def catP(x,y):
        cat = str(x)+str(y)
        cat2 = str(y) + str(x)
        if cat in s and cat2 in s:
            return True
        else: return False
    largest=10000    #    len(l)        
    for a in range(0,largest):
        for b in range(a+1,largest):
            if catP(l[a],l[b]):
                for c in range(b+1,largest):
                    if catP(l[a],l[c]) and catP(l[b],l[c]):
                        # print(l[a],l[b],l[c])
                        for d in range(c+1,largest):
                            if catP(l[a],l[d]) and catP(l[b],l[d]) and catP(l[c],l[d]):
                                for e in range(d+1,largest):
                                    if catP(l[a],l[e]) and catP(l[b],l[e]) and catP(l[c],l[e]) and catP(l[d],l[e]):
                                        print(l[a],l[b],l[c],l[d],l[e])                       #13 5197 5701 6733 8389
# a = [0]*20        
# while len(set(a)) != len(a):
    # u = []
    # for i in range(len(a)):
        # if a[i] in u:
            # a[i] += 1
            # print(a)
            # break
        # else:
            # u.append(a[i])