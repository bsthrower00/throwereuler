#double base palindromes
# print(bin(585)[2:])
def isPalin(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False 

sum = 0
for i in range(1_000_001):
    if isPalin(i) is True and isPalin(bin(i)[2:]) is True:
        sum += i
print(sum)

# b = 0
# b+= i for i in range(1_000_001) if isPalin(i) is True and isPalin(bin(i)[2:]) is True
# print(b)