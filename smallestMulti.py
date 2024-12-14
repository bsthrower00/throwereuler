smallest multiple
def checkMulti(n,m):
    for i in range(m):
        if n % m != 0:
            return False
        else:
            return True 
            
def smallestMulti(n,m):            
    while checkMulti(n,m) is False:
        n += 1
        checkMulti(n,m)
    print(n)
smallestMulti(1,20)

#finished by hand
#2^4*3^2*5*7*11*13*17*19, product of all prime factors