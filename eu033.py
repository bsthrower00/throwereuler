#Digit cancelling fractions
def cancel(a,b):
    a,b = str(a),str(b)
    for i in a:
        # print(i)
        if i == '0':
            return False,0,0
    for i in b:
        # print(i)
        if i == '0':
            return False,0,0
    for i in range(2):
        for j in range(2):
            # print(a[i],b[j])
            if a[i]==b[j]:
                return True,abs(i-1),abs(j-1)
    return False,0,0

list = []

for n in range(10,100):
    for d in range(10,100):
        c,i,j = cancel(n,d)
        # print(n,d,type(n),type(d))
        if n<d and c:
            l1,l2 = [],[]
            n2,d2 = str(n),str(d)
            for a in n2:
                l1.append(a)
            for a in d2:
                l2.append(a)
            l1,l2 = l1.pop(i),l2.pop(j) 
            # print(l1,l2)
            if int(n2)/int(d2) == int(l1[0])/int(l2[0]):
                list.append([n,d])
                
print(list)                