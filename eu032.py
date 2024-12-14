#Pandigital products

numSet = set([1,2,3,4,5,6,7,8,9])
def checkPan(n):
    s,l = '',[]
    i = 1
    while len(s) < 9:
        s += str(n * i)
        i += 1
    for letter in s:
        l.append(int(letter))
    if set(l).intersection(numSet) == numSet and len(l) == 9:
        return True
    else:
        return False

panSet = []
for i in range(1,9999):
    for j in range(1,9999):
        
        p = i * j
        s = str(i)+str(j)+str(p)
        if len(s) >9:
            break
        elif len(s) == 9:
            if checkPan(s):
                panSet.append(p)
                print(i,j,p)
            # break
        # else:
            # print(i,j)
panSet = set(panSet)
print(sum(panSet))           
        


        
# i = 54
# j = 16
# p = i * j
# s = str(i)+str(j)+str(p)
# print(s,len(s))