#integer right triangles
import time
start = time.time()
def isInt(n):
    a = int(n)
    if a == n:
        return True
    else: return False
    
def getB(a,p):
    return (((p*a)-((p**2)/2))/(a-p))

def findTriples(p):
    triples = []
    a = 1
    b = getB(a,p)
    while a < b:
        if isInt(b) is True and b > 0:
            # print(a,b,(a**2+b**2)**.5)
            triples.append([a,b,(a**2+b**2)**.5])
        a += 1
        b = getB(a,p)
    return triples        
 
most = 0 
for i in range(5,1001):
    if len(findTriples(i)) > most:
        most = len(findTriples(i))
        print(i)
end = time.time()
print("The time of execution of above program is :", end-start)