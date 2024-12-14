def EvenFibSum(first,second,summ):
    nextdig = first + second
    if 4000000 > (nextdig):
        if (nextdig) % 2 == 0:
            summ += nextdig
        EvenFibSum(second, nextdig,summ)
    else:
        print('sum is ',summ)
EvenFibSum(0,1,0)        