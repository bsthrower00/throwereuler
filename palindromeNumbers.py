#find if a num is a palindrome
## [::-1] to reverse a string
def isPalin():
    greatest = 0
    for i in range(999,100,-1):
        for p in range(999,100,-1):
            if str(i * p) == str(i*p)[::-1] and (i*p) > greatest:
                greatest = i*p
    print(greatest)            
isPalin()               