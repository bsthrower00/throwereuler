#coded traingle numbers
def nameScore(name):
    sum2 = 0
    for letter in name:
       sum2 += ord(letter) - 64
    return int(sum2) 

def checkTri(n):
    a = (-1) + (1+8*n)**.5 
    # print(a)
    if int(a) == a:
        return True
    else: return False 

  
    # print(checkTri(i),i)  
sum = 0  
with open('p042_words.txt','r') as f:
    a = f.readline()
    a = a.split(',')
    for p in range(len(a)):
            a[p] = a[p][1:-1]
    for word in a:
        if checkTri(nameScore(word)) is True:
            sum += 1
print(sum)            