#Lexicographic permutations
perms = []
lis = []
for a in range(10):
    for b in range(10):
        if b != a:
            for c in range(10):
                if c!= a and c!=b:
                    for d in range(10):
                        if d!=a and d!=b and d!=c:
                            for e in range(10):
                                if e!=a and e!=b and e!=c and e!=d:
                                    for f in range(10):
                                        if f!=a and f!=b and f!=c and f!=d and f!=e:
                                            for g in range(10):
                                                if g!=a and g!= b and g!=c and g!= d and g!=e and g!=f:
                                                    for h in range(10):
                                                        if h!=a and h!= b and h!=c and h!= d and h!=e and h!=f and h!=g:
                                                            for i in range(10):
                                                                if i!=a and i!= b and i!=c and i!= d and i!=e and i!=f and i!=g and i!=h:
                                                                    for j in range(10):
                                                                        if j!=a and j!= b and j!=c and j!= d and j!=e and j!=f and j!=g and j!=h and j!= i:
                                                                            perms.append(str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j))
                                       
perms.sort()
print(len(perms))  
print(perms[1_000_001])              
                
# lis = []
# for i in range(0,1000000000):
    # lis.append(i)
# print(len(lis))    