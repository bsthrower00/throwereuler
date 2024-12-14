#circular primes
from functools import reduce
def prime(n):
    if n == 0 or n == 1:
        return False
    step = 2 if n%2 else 1
    facSet = list(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**.5)+1, step) if n % i == 0)))
    # facSet.pop(1)
    # print(facSet)
    if len(facSet) == 2:
        return True
    else:
        return False
     

     
# def rotate(n,lis=[]):
    # if n in lis:
        # return lis
    # else:
        # lis.append(n)
        # string = ''
        # for i in range(1,len(str(n))):
            # string += str(n)[i]
        # string += str(n)[0]
        # return rotate(int(string),lis)
def rotate(N):
    lis = []
    for p in str(N):
        lis.append(int(p))
    # print(lis,'g')
    output = []
    for i in range(len(lis)):
        output.append(lis[i:] + lis[:i])
    for a in range(len(output)):
        b = ''
        for c in output[a]:
            b += str(c)
        output[a] = int(b)
    return output



# for i in range(100):
    # l = []
    # print(rotate(i),l)
# print(rotate(12345))   
        
c = 1
for i in range(100):
    check = False
    while check is False:
        for digit in str(i):
            if int(digit) == 2 or int(digit) == 5 or int(digit) == 0 or int(digit) == 4 or int(digit) == 6 or int(digit) == 8 or int(digit) == 9:  
                check = True
        print(i)
        check = True
    # print(i)
    # if prime(i) is True:
        # lis = rotate(i)
        # L = []
        # for a in range(len(lis)):
            
            # if prime(lis[a]) is True:
                # L.append(a)
        # if len(L) == len(lis):
            # c += 1
print(c)
