# #mex seq
rounds =1500

s = set([])
s2 = set([])
s3 = set([])
jprev = 0
jiprev =0
sumprev = 0
sums = {}
for n in range(1,rounds+1):
    if n-1 in (1,5,21,85,341,1365,5461): #sums of n^4
        print('#####################################')
        # print(sorted(sums.items(),key = lambda item: item[1]))
        for item in sums:
            print(item)
        sums = {}
        print('#####################################')
    i = 1
    while i in s or i in s2 or i in s3:
        i += 1
    s.add(i)
    j = i+1 

    while j in s or j^i in s or j in s2 or j in s3 or j^i in s2 or j^i in s3:
        j += 1
    s2.add(j)
    s3.add(j^i)
    curs = i + j + (i^j)
    
    sumnow = sum(s)+sum(s2)+sum(s3)
    delta = sumnow-sumprev 
    # print(s1,s2,s3)
    # print(n,i,j,j^i,delta) #j - jprev - (j^i) + jiprev)
    if delta in sums:
        sums[bin(delta)] += 1
    else:
        sums[bin(delta)] = 1
    # print(n,j,j - jprev)
    # print(n,j^i,(j^i) - jiprev)#,sum(s2))#+sum(s2)+sum(s3))
    jprev = j
    jiprev = j^i
    sumprev = sumnow
    print(bin(delta))
print(sorted(sums.items(),key = lambda item: item[1]))

# print(sum(s),sum(s2),sum(s3))
# print(sorted(s))
# print('##########################')
# print(sorted(s2))
# print('##########################')
# print(sorted(s3))
# print('##########################')

# def series(n):
    # z = 1
    # for i in range(2,n+1,2):
        # z += 2**i
        # print(z)
    
    # return z

# upper = 10**18
# ex = int(log(upper,2))
# total4 = 2
# summed = 1	
# ct4 = 2
# print('summedIters=',summed)

# while summed+2**ct4 < upper:
    # # print('+',(2**(ct4+1)-1)-2**ct4+1)
    # summed += 2**ct4
    # # print('summedIters=',summed)
    # # total4 += int(sumSeries(2**ct4,2**(ct4+1)-1))
    # ct4 += 1
    # # print('ct4',ct4,sumSeries((2**ct4/2) + 2**ct4,2**(ct4+1)-1))
    # total4 += int(sumSeries(2**ct4,2**ct4/2 + 2**ct4 -1))
    # # total4 += int(sumSeries((2**ct4/2) + 2**ct4,2**(ct4+1)-1))
    # ct4 += 1
    # # print(total4)

# # print(ct4, total4)
# remaining = upper - summed
# print(summed,remaining, 2**ct4)
# # total4 += int(sumSeries(2**ct4, (2**ct4 + remaining)-1))
# ct4 += 1
# print(2**ct4)
# total4 += int(sumSeries(2**ct4, (2**ct4 + remaining)-1))
# print(summed + remaining)
# print(total4)







