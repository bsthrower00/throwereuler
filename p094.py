#almost eqi traingle
upP = 10**9
total = 0 
# for side in range(upP//3+1):
    # pass

# maxP = 10**9  #2a + b
# maxS = maxP/2
# maxA = maxP // 3
# maxB = maxP // 3 + 1
# maxR = (maxS - maxA)*((maxS-(maxS-maxB))**.5)
# print(maxR)

for i in range(1,10_000_000):
    if float.is_integer((3*i**2+i)**.5 ):
        total += 1
print(total)