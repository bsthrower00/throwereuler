#p92 square digit chains
c = 0
for i in range(1,10_000_001):
	if i%10000 == 0:
		print(i)
	num = i
	while num not in [1,89]:
		s = 0
		for l in str(num):
			s += int(l)**2
		num = s
	if num == 1:
		c += 1
	else: 
		c += 0
		
print(c)
