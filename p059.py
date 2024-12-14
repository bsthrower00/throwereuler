#xor decrpy
from itertools import combinations, permutations
lower = []    
for i in range(97,123):
    lower.append(i)    
key = list(permutations(lower,3))
# print(list(key)[5][1])
# print(lower)
# print(chr(key[2942][0])+chr(key[2942][1])+chr(key[2942][2]))


d = ''
sum = 0
with open('p059_cipher.txt','r') as f:
    a = f.readline()
    a = a.split(',')
    for c in range(len(a)):
        sum += int(a[c])^key[2942][c%3]
    print(sum)    
    # for k in range(len(key)):  
        # # print(k)
        # for c in range(len(a)):
            
            # d += chr(int(a[c])^key[k][c%3])  ### combo k = 2942 is corret
            # # print(decrpt[1:100])
        # d = d.split(' ')
        # if len(d) > 10 and d[0].isalpha() and d[1].isalpha() :
            # print(k,str(c)+'\n')
            # print(d)
        # d = ''
       


    
# with open('p042_words.txt','r') as f:
    # a = f.readline()
    # a = a.split(',')
    # print(a)
    # for p in range(len(a)):
            # a[p] = a[p][1:-1]
    # for word in a:
        # if checkTri(nameScore(word)) is True:
            # sum += 1