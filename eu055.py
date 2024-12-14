#Lychrel numbers
def checkPal(n):
    if str(n) == str(n)[::-1]:
        return True
    else: return False
    
    
def lych(n,i=0):
    # if str(n)[0] == str(n)[len(str(n))-1]:
    print(i,n)
    if i != 0 and checkPal(n):
        
        return True
    elif i == 50:
        return False
    else:
        i +=1
        return lych(n+int(str(n)[::-1]),i)
# print(lych(10677 ))
        
c=0       
for i in range(0,10_001):
    if lych(i)is False:
        c+=1
print(c)