#p079 password
d1 = {n:0 for n in range(10)}
d2 = {n:0 for n in range(10)}
d3 = {n:0 for n in range(10)}
with open("0079_keylog.txt",'r') as f:
	for line in f:
		# print(line.strip())
		d1[int(line[0])] += 1
		d2[int(line[1])] += 1
		d3[int(line[2])] += 1
		if '6' in line:
			print(line)
		
print(d1)
print(d2)
print(d3)