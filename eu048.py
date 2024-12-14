#self powers!
sum = 0
for i in range(1,1001):
    sum += i ** i
print(sum)
print(str(sum)[len(str(sum))-10:])