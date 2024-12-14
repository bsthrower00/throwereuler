#factorial sum  
def factorial(n,c=1):
    if n == 1:
        return c
    else:
        c *= n
        return factorial(n-1,c)    

def facsum(l):
    sum = 0        
    # p = input('what num? ')
    for i in str(factorial(int(l))):
        sum += int(i)
    # print(sum)    
    return sum
    
  
for i in range(1,100):
    print(i, facsum(i))