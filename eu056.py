#powerful digit sum
high = 0 
for i in range(101):
    print(i)
    for p in range(101):
        l = []
        for j in str(i**p):
            l.append(int(j))
        if sum(l) > high:
            high = sum(l)
print(high)