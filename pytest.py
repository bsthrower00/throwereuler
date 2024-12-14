#pytest

def recCyc(n):
    q = str(int(1000**1000//n))
    for i in range(len(q)):
        u = q.find(q[i:i+5])
        if u != i:
            return(i-u)

t = 0
v = 0
for i in range(3,1000,2):
    if recCyc(i) > v:
        v = recCyc(i)
        t = i

print(t,v)