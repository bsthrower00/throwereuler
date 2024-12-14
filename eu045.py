#tri,pent,hex numbers
def isInt(n):
    if n == int(n):
        return True
    else: return False
    
def checkPent(n):
    a = (1 +(1 + (24 *n))**.5)/6
    if  isInt(a) is True:
        return True
    else: return False 
    
def checkHex(n):
    a = (1 + (1 + (8*n))**.5)/4
    if isInt(a) is True:
        return True
    else: return False 
    
def checkTri(n):
    a = (-1 + (1 + 8*n)**.5)/2
    if isInt(a) is True:
        return True
    else: return False 
    
def genPent(n):
    return int(n*(3*n-1)/2)
    
    
# t = [1,3,6,10,15]
# p = [1,5,12,22,35]
# h = [1,6,15,28,45]
# for i in h:
    # print(checkHex(i))
    
# for i in range(1,10):
    # print(genPent(i))
    
for i in range(1,10_000_000):
    a = genPent(i)
    if checkHex(a) is True:
        print(a)