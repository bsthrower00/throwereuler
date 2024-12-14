#mersenne prime digits
def findP(n,rep):
    if rep == 0:
        return str(n[-10:])
    else:
        print(n,rep)
        return findP((int(str(n)[-10:]))*2,rep-1)
        
# print(findP(2,7830457))
num = 2
for i in range(1,7830457):
    num = int(str(num)[-11:])*2
    if i > 7830450:
        print(num,i)
#5203706140164096