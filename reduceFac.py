#reduce fac
def reduce(n,d):
    if n/d == int(n/d) or n==1 or d== 1:
        return n,d
    elif n<d:
        a=n 
    else:
        a=d
    for i in range(2,int(a+1)):
        if n%i ==0 and d%i ==0:
            print(i,n,d)
            return reduce(n/i,d/i)
            
    return n,d

# print(reduce(795894761733579, 562949953421312))

# def reciprocal_cycle(n):
    # q = str(int(10**1000//n))
    # for i in range(len(q)):
        # u = q[i:i+5]
        # if q.find(u) != i:
            # return(i-q.find(u))

# t = 0
# v = 0
# for i in range(2,1000):
    # if reciprocal_cycle(i) > v:
        # v = reciprocal_cycle(i)
        # t = i

# print(t,v)