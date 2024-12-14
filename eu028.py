#number spiral diagonals
# size = 1001
# grid = [None] * size
# for i in range(size):
    # grid[i] = [None] * size

# start = [size//2 + 1, size//2 + 1]
# for i in range(1,size**2 + 1):
    # if grid[start[0],start[1]+1] is None:
        # grid[start[0],start[1]] = i


sum = 1   
i = 3    
p=2
for i in range(3,1002,2):
    sum += 4* i**2 - 6*p
    p += 2
print(sum)