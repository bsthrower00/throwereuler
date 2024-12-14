#name scores + sorting by alphebetical order 
def nameScore(name):
    sum2 = 0
    for letter in name:
       sum2 += ord(letter) - 64
    return sum2   
    
# print(nameScore('COLIN'))

def sortNames():
    sum = 0
    with open('p022_names.txt','r') as f:
        a = f.readline()
        a = a.split(',')
        for p in range(len(a)):
            a[p] = a[p][1:-1]
        a = sorted(a)
        for namePos in range(len(a)):
            sum += nameScore(a[namePos]) * (namePos + 1)
    print(sum)            
sortNames()        
