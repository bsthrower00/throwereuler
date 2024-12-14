#longest collatz chain under 1million
def collatz(n ,c=1):
    # print(c,n)
    if int(n) == 1:
        return c
    elif n % 2 == 0:
        return collatz(n/2, c+1)
    else:
        return collatz(3*n+1, c+1)
        

def longColl():
    longest = 0
    for i in range(1,1_000_000): 
        print(i) 
        if collatz(i) > longest:
            longest = collatz(i,0) 
            which = i
    print(which, longest, 'finished')

longColl()    

# print(collatz(33))