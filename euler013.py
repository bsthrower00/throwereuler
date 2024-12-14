#large sum
sum = 0
with open('largesum013.txt','r') as f:
    for i in range(100):
        sum += int(f.readline())
    print(str(sum)[:10])
