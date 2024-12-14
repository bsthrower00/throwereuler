#digit fifth powers
s = 0
for i in range(2,1_000_000):
    su =0
    for digit in str(i):
        su += int(digit)**5
    if su == i:
        s += i
        print(i)
print(s,'is sum')