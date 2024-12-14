#arith expressoins
#Find the set of four distinct digits,a,b,c,d, for which the longest set of consecutive positive integers,1 to n, can be obtained, giving your answer as a string: abcd.
from itertools import permutations, product
	

	
def op(a,b,c):
	if c == '*':
		return a*b
	elif c == '/':
		return a/b
	elif c == '-':
		return a-b
	else:
		return a+b
	
	
ops = product(['*','/','+','-'],repeat = 3) ##Should use postfix notation. this leave out (a+b)*(c+d)
opsList = []
for o in ops:
	opsList.append(o)
# print(opsList[9][1])

n = 15 
best = [0,0,0,0,0]
for w in range(1,n):
	print(w)
	for x in range(w,n):
		for y in range(x,n):
			for z in range(y,n):
				# print(w,x,y,z)
				perm = permutations([w,x,y,z])
				s = set([])
				m = 0
				for i in perm:
					for oper in opsList:
						j = op(i[0],i[1],oper[0])
						j = op(j,i[2],oper[1])
						j = op(j,i[3],oper[2])
						if int(j) == j:
							if j > 0:
								s.add(j)
				
					# print(w,x,y,z,s,'\n')
				for i in range(1,65):
					if i in s:
						m += 1
					else:
						if z == 8 and w == 1 and y == 5 : print(i,w,x,y,z,s,'\n')
						break
				if m > best[4]:
					best = [w,x,y,z,m]
						
print(best)

# a = set([])
# print(a)
# a.add(6)
# print(a)						