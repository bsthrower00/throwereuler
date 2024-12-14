#permuted mutiples
def setCheck(p):
    s=set([])
    for a in str(p):
        s.add(a)
    return s
for i in range(1,100_000_000):

    if len(str(i)) == len(str(i*6)):
        for p in range(2,7):
            if setCheck(i) != setCheck(i*p):
                break
            if p == 6:
                print(i,2*i,3*i)