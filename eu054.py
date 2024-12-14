#poker hands
def handList(h):
    for i in range(len(h)):
        h[i] = [h[i][0],h[i][1]]
    return h 
    
    
def faceToNum(h):
    for i in range(len(h)):
        # print(h[i][0])
        if h[i][0] == 'J':
            h[i][0] = 11
        elif h[i][0] == 'Q':
            h[i][0] = 12
        elif h[i][0] == 'K':
            h[i][0] = 13
        elif h[i][0] == 'A':
            h[i][0] = 14
        else: h[i][0] = int(h[i][0])
    return h 
        

    
    
def checkFlush(H):
    a = [[],[],[],[]]
    for card in H:       
        if card[1] == 'S':
            a[0].append(card[0])
        elif card[1] == 'C':
            a[1].append(card[0])
        elif card[1] == 'H':
            a[2].append(card[0])
        elif card[1] == 'D':
            a[3].append(card[0])
    flush = False
    highest = 0
    for i in a:
        if len(i) > 3:
            flush = True
            for j in i:
                if j> highest:
                    highest=  j
    return flush, highest 
    
    

    
def checkStraight(h):
    highest = highestVal(h)
    l = []
    st = True
    for i in h:
        l.append(i[0])
    for i in range(1,5):
        if highest - i not in l:
            st = False
            # print(highest-i)
    # print(l,highest )
    return st

def mostCards(h):
    s = set([])
    for i in h:
        s.add(i[0])
    print(s,len(s))
    
    
    
a = [[2, 'S'], [2, 'S'], [3, 'S'], [3, 'S'], [4, 'S']]
print(mostCards(a))    
        
    
def checkPairs():
    pass
    
def highestVal(h):
    highest = 0
    for card in h:
        if card[0] > highest:
            highest = card[0]
    return highest


def evalHand(h):
    fb,fv = checkFlush(h)
    s = checkStraight(h)
    p,v = checkPairs(h) #number of pairs, value... might need to add values to others
    h = highestVal(h)
    mc = mostCards(h)
    if s and f and h==14:
        return 9
    elif s and f:
        return 8
    elif mc == 4:
        return 7
    elif mc == 3 and p == 2:
        return 6
    elif f:
        return 5
    elif s:
        return 4
    elif mc == 3:
        return 3
    elif p == 2:
        return 2
    elif p == 1:
        return 1
    else:
        return 0
 
 
