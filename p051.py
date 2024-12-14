from itertools import combinations 

primes = set([])
with  open('primes10000.txt', 'r') as file:
	for line in file:
		line = line.strip()
		if len(line) != 5:
			line = "0" * (5 - len(line)) + line
		primes.add(line)
# print(primes)		

for i in range(10):
	pass				
	
iters = [0,1,2,3]
k = 2 
combs = combinations(iters,k)
combs_list = list(combs)
print(combs_list)
# for combo in combs_list:
fail = 0
	
for i in range(1000):
	i = str(i)
	if len(i) != 3:
			i = "0" * (3 - len(i)) + i
	# if int(i[2])  in [1,3,7,9]:
	# print(i)
	for p in combs_list:
		for q in range(10):
			