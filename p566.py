#birthday cake

# cake = [0,False,10,True,130,False,220,True,280,False]
# cake = [0,False,10,True,120,130,False,220,True,280,False]


cake = [0,True]
def cut(angle,start):
    if len(cake)==3: #no cuts
        return [0,False,angle,True]
    
    #first find start and end points of cut. Start is given.
    #start = start
    end = (start+angle)%360
    #find SubF, SubU and define state of slice (all frosted, all unfrosted, forsting first, or unf first
    #to begin find what starts the slice. 
    
    extraSlice = False
    try: first = cake.index(start)+1  #index of first state
    except: #wanted slice is not indexed yet.
        cur = 0
        for i in range(0,len(cake),2):
            if cake[i]<start:
                curr = i
            else: break
        cake.insert(i,start)
        cake.insert(i+1,cake[i-1])
        extraSlice = True
        # print(cake)
        first = first = cake.index(start)+1
    
    twoSlice = False
    if cake[(first+1)%len(cake)] < end:
        twoSlice = True
        

        #ex prev is same, next is same
        #cake = [300, True, 330] ~ (1.7,4)
        #flip 40 - 110 Start was 40. index was deleted using cur system. 
        #cake = [40,True,100,False,300,True,330,False]
       
    if extraSlice is True: #same color preceedes
        #ffff,ffuf,fffu,ffuu,uuuf,uuff,uuuu,uufu
        if twoSlice is True:
            #[20,F,90,F,160,T,190,F,250,T,280,F,350,T]
            #cut 90-190  ~1.7r, 12-13
            #[20,F,(90F120)120,T,190,F,250,T,280,F,350,T]
            
        
    else: 
        pass





    
    #start = 0, first = 1,  cake[2%4=2] = angle (check)
    newCake = cake
    if twoSlice:
        if cake[first]: #first piece is  frosted
            pass
        else:           #second piece is frosted
            pass
        
        #ex surrounded by both sides by opposite
        #cake = [10,False,100,True,190,False,200,True,280,False,330,True] ~(1.7rad,15)
        #flip 10 - 100. start was 10, indexed at 0, 
        #cake [190,False,200,True,280,False,330,True]~(1.7rad,16)
        
        #ex prev is opposite, next is same
        #cake = [160,False,210,True,230,False,330,True] ~(1.7rad,18)
        #flip 330 - 40. Start was 330, indexed at 6
        #cake = [40, True, 160,False,210,True,230,False] ~(1.7rad,19)
        
        
    else: #single color
        if cake[first]: #Frosted
            pass
        else:           #unfrosted
            pass
            
# cake = [60,False,150,True,190,False,260,True,330,False,350,True]
# cut(80,250)