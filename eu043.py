#substring pandig divisibility
from itertools import permutations
perm = list(permutations([0,1,2,3,4,5,6,7,8,9]))
primeList = [2,3,5,7,11,13,17]
sum = 0


for item in perm:
    dig = 0 
    for i in range(0,10):
        # print(item[i])
        dig += item[i] * 10**(9-i)
    a = 0
    for i in range(7):
        newDig = int(str(dig)[i+1:i+4])
        if newDig%primeList[i] == 0:
            a += 1 
        else: break 
    if a == 7:
        sum += dig
        print(dig)
print(sum)