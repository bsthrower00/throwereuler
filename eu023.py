#non abundant sums
from functools import reduce
def abundant(n):
    step = 2 if n%2 else 1
    facSet = list(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**.5)+1, step) if n % i == 0)))
    facSet.pop(1)
    if sum(facSet) > n:
        return True
    else:
        return False
        
        

        
def listOfAbuns():
    abunList = []
    for i in range(1,28124):
        if abundant(i) is True:
            abunList.append(i)
    return abunList      
print(listOfAbuns())
def abunSumCheck():
    firstList = listOfAbuns()
    secondList = []
    for q in range(1,28124):
        check = False
        for i in firstList:
            if check is True or q < i:
                break
            for p in firstList:
                if check is True or q < p:
                    break
                elif i + p == q:
                    check = True 
                    
        if check is False:
            secondList.append(q)
            print(q)
    return sum(secondList)
    
# print(abunSumCheck()) 

# def bySub():
    # abunlist0 = []
    # abunList = listOfAbuns()
    # for i in abunList:
        # for p in abunList:
            # if i < p:
                # abunlist0.append(p-i)
    # abunSet = set(abunlist0)
    # newList = []
    # for i in range(1,28124):
        # newList.append(i)
    # newSet = set(newList)    
    # print(abunSet)
    # setDiff = newSet.difference(abunSet)
    # print(setDiff)
    # print(sum(list(setDiff)))
    # print(sum(setDiff))
     
    
# bySub()

def tryThree():
    list0 = []
    abunList = listOfAbuns()
    print(len(abunList))
    for i in abunList:
        for p in abunList:
            if i + p < 28123:
                list0.append(i+p)
            else:
                break
    abunSet = set(list0)
    # print(abunSet)
    newList=[]
    for i in range(1,28124):
        newList.append(i)
    fullSet = set(newList)
    setDiff = fullSet.difference(abunSet)
    print(setDiff)
    # print(sum(list(setDiff)))
    print(sum(setDiff))
# # # tryThree()        
                