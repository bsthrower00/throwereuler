def sumOfMultiples():
    summ = 0
    for i in range(0,1000):
        if i % 5 == 0 or i % 3 == 0:
            summ = i + summ
    return summ        
print(sumOfMultiples())