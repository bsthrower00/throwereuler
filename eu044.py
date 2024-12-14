#pentagon numbers
def checkPent(n):
    a = (1 +(1 + (24 *n))**.5)/6
    if n < 0:
        return False
    # print(a)
    elif int(a) == a:
        return True
    else: return False 
def genPent(n):
    return int(n*(3*n-1)/2)
    
smallest = 999999

l = []
for i in range(1,10000):
    l.append(genPent(i))
for item1 in l:
    for item2 in l:
        if item2 > item1: 
            if checkPent(item1+item2) and checkPent(item2-item1):# is True and checkPent(greater+lesser) is True:
                print(item1,item2)
                if item2-item1 < smallest:
                    smallest = item2-item1
        
         

# for i in range(1,1000):
    # x = genPen(i)
    # for p in range(1,1000):
        # y = genPen(p)
        # if y < x:
            # z = y
        # else: 
            # z=x 
            # x=y
        # if checkPent(x-z) is True and checkPent(x+z) is True:
            # print(x,y)
            # if abs(x-y) < smallest:
                # smallest = x-y 
print(smallest)
