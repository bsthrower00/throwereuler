#find trigangle number with high number of divisors
from functools import reduce

def findNumOfDivisors(n):
    divisors=0
    if n%5 != 0 or n%2 != 0:
        return 0 
    for i in range(1,n+1):
        if n%i == 0:
            divisors += 1
    # print('god this is so gay')
    return divisors         
    
def factors(n):
        step = 2 if n%2 else 1
        return len(set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(n**.5)+1, step) if n % i == 0))))    
    
def checkTriangles(num):
    # print('thisisgay')
    summ = sum(range(num+1))
    # print(summ)
    l = factors(summ)
    # print(num,summ,l)
    if l >= 500:
        # print('FINISHED', summ, l)
        return True
    else:
        return False
    # if l > 500:
        # checkTriangles(num+1)
    # else:
        # print(num, 'FINISHED!')


def howmanydivs():
    q = int(input('check num of divs? (enter an integer): '))
    print(findNumOfDivisors(q))
        
# howmanydivs()
for i in range(1,25000):
    if checkTriangles(i) is True:
        summ = sum(range(i+1))
        # print(summ)
        l = factors(summ)
        print(i,summ,l)
        if l >= 500:
            print('FINISHED', summ, l)
        break

                                            #checked 2000-2750 even or mult of 5 only
                                            # 2750 on ending in 0 only