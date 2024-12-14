#digit factorials
def factorial(n,c=1):
    if n == 0:
        return 1
    elif n == 1:
        return c
    else:
        c *= n
        return factorial(n-1,c)    


# print(factorial(0))
lis = []
for i in range(2,999999):
    s = 0
    for p in str(i):
        s += factorial(int(p))
    if s == i:
        lis.append(i)
print(lis)