#1000 dig fib number
def Fib(first,second,count):
    nextdig = first + second
    print(count,len(str(nextdig)))
    if 1000 > len(str(nextdig)):
        Fib(second, nextdig,count+1)
    else:
        print('sum is ',nextdig)
Fib(0,1,1)        