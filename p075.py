#one integer sided right triangles
import math  #math.hypot
upper =int( 1.5*10**6)

L = []
for m in range(2,upper):
    for n in range(m):
        p = 2*m*n + 2*m**2 
        if p > upper:
            break
        elif math.gcd(m,n) == 1 and ((m%2==0 and n%2==1) or (m%2==1 and n%2==0)):
            
            if p < upper:
                k = 1
                while k*p < upper:
                    # print(p)
                    # L.append([k*m,k*n,k*p])
                    L.append(k*p)
                    k = k + 1
c = 0
L.sort()
# print(L)
# print(len(L))
# print(len(L)-len(set(L)))
# for item in L:
    # if L.count(item) == 1:
        # c = c + 1
        # print(c)
# print(c)
if L[0] != L[1]:
    c += 1
if L[len(L)-2] != L[len(L)-1]:
    c += 1
for i in range(1,len(L)-1):
    if L[i] != L[i-1] and L[i] != L[i+1]:
        c += 1
print(c)