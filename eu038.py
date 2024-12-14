#pandigital multiples
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
        return True, int(s)
    else:
        return False, 0

# a,b = checkPan(192)
# print(a,b)
largest = 0
for p in range(9999):
    boole,num = checkPan(p)
    if boole is True and num > largest:
        largest = num
print(largest)        