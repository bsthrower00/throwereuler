#54 poker hands
with open('0054_poker.txt', 'r') as f:
	lines = f.readlines()
	# for line in lines:
		# print(line.strip())
		
def hierarchy(a):
	higher = {'A':'14', '2':'02' , '3':'03' , '4':'04' , '5':'05', '6':'06', '7' :'07', '8' :'08', '9':'09' , 'T':'10' ,'J':'11','Q':'12','K':'13' }
	return higher.get(a)
	
def kicker(hand,n):
	# print(hand)
	l = []
	if n == 3:
		for i in range(n):
			l.append(hand[i+1][0])
	else:
		for i in range(n):
			l.append(hand[i][0])
	# print(l)
	l.sort(reverse=True)
	toReturn = ''
	for item in l:
		# print(item)
		toReturn += item
	return toReturn
		

def colorMatch(hand):
	colorSet = set([])
	for letter in range(1,len(hand),3):
		colorSet.add(hand[letter])
	if len(colorSet) == 1:
		return True
	else: return False 

straights = \
set([ 'A' , '2' , '3' , '4' , '5' ]) ,\
set([ '2' , '3' , '4' , '5' , '6' ]) ,\
set([ '3' , '4' , '5' , '6' , '7' ]) ,\
set([ '4' , '5' , '6' , '7' , '8' ]) ,\
set([ '5' , '6' , '7' , '8' , '9' ]) ,\
set([ '6' , '7' , '8' , '9' , 'T' ]) ,\
set([ '7' , '8' , '9' , 'T' , 'J' ]) ,\
set([ '8' , '9' , 'T' , 'J' , 'Q' ]) ,\
set([ '9' , 'T' , 'J' , 'Q' , 'K' ]) ,\
set([ 'T' , 'J' , 'Q' , 'K' , 'A' ]) #this was the worst part of the code to write and it wasnt even coding
# print(straights)


def straight(hand):
	nums = set([])
	for letter in range(0,len(hand),3):
		nums.add(str(hand[letter]))
	if len(nums)==5 and set(nums) in straights:
		return True
	else: return False


def pairsPlus(hand):
	# print(hand)
	nums = {'A':0 , '2':0 , '3' :0, '4' :0, '5':0,'6' :0, '7' :0, '8' :0, '9' :0, 'T':0,'J':0,'Q':0,'K':0}
	for letter in range(0,len(hand),3):
		nums[hand[letter]] += 1
		
	nums2 = {}
	for key in nums:
		nums2[hierarchy(key)] = nums.get(key)	
	nums = nums2
	nums = sorted(nums.items(),key=lambda item: item[1],reverse=True)
	l = []
	if nums[0][1] == 4:
		return ['quads', nums[0][0] + nums[1][0]] 
	elif nums[0][1] == 3:
		if nums [1][1] == 2:
			return ['fh', nums[0][0]+ nums[1][0]]
		else: 
			toReturn = nums[0][0]+ nums[1][0] + nums[2][0]if int(nums[1][0])>int(nums[2][0]) else nums[0][0]+ nums[2][0] + nums[1][0]
			return ['trips', toReturn]
	elif nums[0][1] == 2:
		if nums [1][1] == 2:
			if int(nums[0][0])>int(nums[1][0]):
				toReturn = nums[0][0]+ nums[1][0]
			else: 
				toReturn = nums[1][0]+ nums[0][0]
			return ['2p', toReturn + nums[2][0]]	
		else: return ['1p' , nums[0][0] + kicker(nums,3)]
	else: return ['hi', kicker(nums,5)]
	
	



def scoreHand(hand):
	score = 0
	pairs = pairsPlus(hand)
	# print(pairs)
	if pairs[0] == 'quads':
		score = '7' + '.' +pairs[1]
	elif pairs[0] == 'fh':
		score = '6' + '.' +pairs[1]
	elif colorMatch(hand):
		if straight(hand):
			score = '8' + '.'+ pairs[1]
		else: 
			score = '5' + '.'+ pairs[1]			
	elif straight(hand):
		score = '4'+ '.'+ pairs[1]
	elif pairs[0] == 'trips':
		score = '3' + '.' +pairs[1]
	elif pairs[0] == '2p':
		score = '2' + '.' +pairs[1]
	elif pairs[0] == '1p':
		score = '1' + '.' +pairs[1]
	else: 
		score = '0.' + pairs[1]
	return float(score)
		
	
wins = 0		
for play in lines:
	if scoreHand(play[0:15]) > scoreHand(play[15:]):
		wins += 1
print(wins)

	
	
# hierarchy(1,1)

# dict = {'a':1,'b':2}
# print(True if dict['c'] else False)
# nums = {'A':0 , '2':0 , '3' :0, '4' :0, '5':5,'6' :0, '7' :0, '8' :0, '9' :0, 'T':0,'J':0,'Q':0,'K':0}
# nums2 = {}
# for key in nums:
	# nums2[hierarchy(key)] = nums.get(key)
# print(nums2)

# print(nums)
# print(dict.get('b'))


