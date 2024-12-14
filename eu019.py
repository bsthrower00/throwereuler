#factorial sum
def factorial(n,c = 1):
    if n = 1:
        return c
    else: 
        c = c * n
        factorial(n-1, c)
        
        
print(factorial(5))