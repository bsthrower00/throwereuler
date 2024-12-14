#tripleFinder

def finder():
    for a in range(500):
        for b in range(500):
            if (a + b + (a**2+b**2)**.5) == 1000:
                return a,b
                
print(finder())
#200*375*425 =                 