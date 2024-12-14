#Square root convergents
from fractions import Fraction
# print(reduce(15,10))
# def f(i,n=0):
    # if i == -1:
        # return n 
    # else:
        # i-=1
        # if n == 0:           
            # return f(i,3/2)
        # elif n == 3/2:          
            # return f(i,7/5)
        # else:      
            # # print('n is: ',n)
            # return f(i,1+(1/(1+n)))
            
            
# def f(i,n=0,d=0):
    # if i == -1:
        # return Fraction(n,d)
    # else:
        # i-=1
        # if n == 0:           
            # return f(i,3,2)
        # elif n == 3/2:          
            # return f(i,5,3)
        # else:      
            # # print('n is: ',n)
            # return f(i,2+Fraction(n,d),1+Fraction(n,d))            
       
# c = 0       
# for i in range(0,1001):
    # a =f(i,0)    
    # if len(str(a.numerator)) > len(str(a.denominator)):
        # c+=1
        # print(i,c)
# print(c)
   
   
# s = 'i like to eat pie'
# print(s[:-1])
# a  = Fraction(5,3)
# a  = a+1
# print(a,type(a))


def expand(n):
    (num,den) = (1,2)
    for i in range(1, n): (num,den) = (den,num + 2*den)
    return (num,den)

def nth(n):
    (num,den) = expand(n)
    return len(str(num+den)) > len(str(den))

counter = 0
for n in range(0, 1000): 
    if nth(n+1): counter += 1
print (counter)