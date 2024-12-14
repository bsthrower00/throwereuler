# #coin sums
# s = 1
# for g in range(0,201,100):
    # for f in range(0,201,50):
        # if f+g > 200:
            # break
        # for e in range(0,201,20):
            # if f+g+e > 200:
                # break
            # for d in range(0,201,10):
                # if f+g+e+d > 200:
                    # break
                # for c in range(0,201,5):
                    # if f+g+e+d+c > 200:
                        # break
                    # for b in range(0,201,2):
                        # if f+g+e+d+c+b > 200:
                            # break
                        # for a in range(1,201):
                            # if a+b+c+d+e+f+g == 200:
                                # s += 1
                                # print(a,b,c,d,e,f,g)
# print(s)                               


#Project Euler Problem 31

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*target
# print(ways,len(ways))
for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]
        print(ways)

print("Ways to make change =", ways[target])

#https://www.geeksforgeeks.org/dynamic-programming/
#https://blog.dreamshire.com/project-euler-31-solution/