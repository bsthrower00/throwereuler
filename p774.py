#conjunctive sequences
# print(10|12)
def conj(a):
    for i in range(1,len(a)):
        if (a[i])&(a[i+1]) == 0:
            return False
        else: return True 
l = []        
for i in range(11):
    for j in range(11):
        l.append(