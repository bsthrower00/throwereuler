# #mex seq
rounds =85

s = set([])
s2 = set([])
s3 = set([])

for n in range(1,rounds+1):
	if n%1000 == 0:
		print(n)
	i = 1
	while i in s or i in s2 or i in s3:
		i += 1
	s.add(i)
	j = i+1 
	
	while j in s or j^i in s or j in s2 or j in s3 or j^i in s2 or j^i in s3:
		j += 1
	# print(i,j,j^i)	
	s2.add(j)
	s3.add(j^i)
	# print(s)

print(sum(s),sum(s2),sum(s3))
# print(sorted(s))
# print('##########################')
# print(sorted(s2))
# print('##########################')
# print(sorted(s3))
# print('##########################')


# s = set([])

# for n in range(1,rounds+1):
	# if n%1000 == 0:
		# print(n)
	# i = 1
	# while i in s:
		# i += 1
	# s.add(i)
	# j = i+1 
	
	# while j in s or j^i in s:
		# j += 1
	# print(i,j,j^i)	
	# s.add(j)
	# s.add(j^i)
	# # print(s)


# print(sorted(s))
# print(len(s))

# print('##########################')
# l = []
# z = 0
# for q in range(100000):
	# if q not in s:
		# l.append(q)
		# z+=1
	# if z ==10000 or q > max(s):
		# break
# print(l, len(l))
# # print(sum(s)%1000000007)


from math import log
# print(log(64,2))
# print(int(6.6))
#I want the sum of the first 10^18 didgets in each of the 3 sequences
def sumSeries(start,end):
	return(end-start + 1)/2*(start + end)
	
# sum1 = 0
# for i in range(0,59,2):
	# sum1 += sumSeries(2**i,2**(i+1)-1)
	# print(i,sum1)
# print(sum1)
# for i in range(0,59,)

summedNums = 1
total = 1
ct = 2
while summedNums <10**17:
	total += sumSeries(2**ct,2**(ct+1)-1)
	summedNums += 2**(ct+1) -2**ct
	ct += 2
	print(total, summedNums)

summedNums2 = 1
total2 = 2
ct2 = 3
while summedNums2 < 10**17:
	total2 += sumSeries(2**ct2,2**ct2/2 + 2**ct2 -1)
	summedNums2 += 2**ct2/2 + 2**ct2 - 2**ct2
	ct2 += 2
	print(total2, summedNums2)

summedNums3 = 1
total3 = 3
ct3 = 3
while summedNums3 < 10**17:
	total3 += sumSeries((2**ct3/2) + 2**ct3,2**(ct3+1)-1)
	# print(2**(ct3+1)-((2**ct3/2) + 2**ct3))
	summedNums3 += (2**(ct3+1)-((2**ct3/2) + 2**ct3))
	ct3 += 2
	print(total3, summedNums3)
	
remaining = 10**18 - int(summedNums)
print(remaining)
print(ct,ct2,ct3)
print((remaining *3 + summedNums+summedNums2+summedNums3)%10**18)
print(int(summedNums2== summedNums))
total += sumSeries(2**ct, 2**ct+remaining)
total2 += sumSeries(2**ct2, 2**ct2+remaining)
total3 += sumSeries((2**ct3/2)+ 2**ct3,(2**ct3/2) + (2**ct3)+remaining)
print((total+total2+total3)%1_000_000_007)









