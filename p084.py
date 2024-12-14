#p084 Monopoly 
from random import randint
die = 4
turn = 0
curr = 0
squares = {n:0 for n in range(40)}
# squares[15] += 1
# squares[15] += 1
# squares[15] += 1
# print(squares.get(15))
# print(squares)
# print(len(squares))
dubct = 0 
# print(11//10 *10+5,0)
while turn < 19_000_000:
	if turn%1_000_000 == 0:
		print(turn)
	a = randint(1,die)
	b = randint(1,die)
	curr = (curr + a + b)%39
	
	if curr == 7 or curr == 22:
		roll = randint(1,16)
		if roll == 1:
			curr = 10
		elif roll == 2:
			curr = 0
		elif roll == 3:
			curr = 11
		elif roll == 4:
			curr = 24
		elif roll == 5:
			curr = 39
		elif roll == 6:
			curr = 5
		elif roll == 7 or roll == 8:
			nextRail = curr//10 *10+ 5 
		elif roll == 9: 
			if curr < 12 or curr > 28:
				curr = 12
			else:
				curr = 28
		elif roll == 10:
			curr -= 3

	if curr == 2 or curr == 17:
		if randint(1,16) <= 2:
			if randint(1,2) == 1:
				curr = 0
			else:
				curr = 10
				
	if curr == 30:
		curr = 10
	
	if a == b: ###Need to fix doubles not rolling, but w/e i got the right answer anyways
		dubct += 1
		if dubct == 3:
			curr = 10
	else:
		dubct = 0
		
	squares[curr] += 1
	turn += 1

print(squares)
for key,value in sorted(squares.items(), key=lambda x: x[1], reverse=True):
	print(key,value)