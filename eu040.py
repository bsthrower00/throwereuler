#Champernowne's constant
import time
start = time.time()
d = ''
for i in range(185188):
    d += str(i)
# s = 1
# while len(d) < 1000000:
    # d += str(s)
    # s += 1    
# print(s)  
product = 1
for i in range(7):
    product *= int(d[10**i])
print(product)
end = time.time()
print("The time of execution of above program is :", end-start)