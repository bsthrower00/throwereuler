import time, math

def M(n, a = 1, b = 2, c = 3, i = 0):
    mod = 10**9 + 7
    if n <= 0:
        return 0
    
    power = pow(4, i)
    if power < n:
        #If power < n we sum our current power and continue with a higher fixed sum
        #M(power) + M(n - power)
        return (M(power, a, b, c, i) + M(n - power, 4*a, 4*b, 4*c, i + 1)) % mod
    elif power == n:
        #We just need to return the sum of the block which starts at (a, b, c) and is power long
        #sum_a = (a + power) // 2 * (a + power - 1) - a * (a - 1) // 2 
        sum_a = (a + power - 1) * (a + power) // 2 - (a - 1) * a // 2 
        #sum_b = 3*power // 2 * (3*power - 1) - 2*power * (2*power - 1) // 2 
        sum_b = (b + power - 1) * (b + power) // 2 - (b - 1) * b // 2 
        #sum_c = 4*power // 2 * (4*power - 1) - 3*power * (3*power - 1) // 2 
        sum_c = (c + power - 1) * (c + power) // 2 - (c - 1) * c // 2  
        return (sum_a + sum_b + sum_c) % mod
    else:
        #If power > n we divide it into our 4 blocks with a lower power
        #Then we sum all the blocks with their respective fixed sums
        s_power = power // 4
        sum_1 = M(min(n, s_power), a, b, c, i - 1) % mod
        sum_2 = M(min(n - 1*s_power, s_power), a + 1*s_power, b + 2*s_power, c + 3*s_power, i - 1) % mod
        sum_3 = M(min(n - 2*s_power, s_power), a + 2*s_power, b + 3*s_power, c + 1*s_power, i - 1) % mod
        sum_4 = M(min(n - 3*s_power, s_power), a + 3*s_power, b + 1*s_power, c + 2*s_power, i - 1) % mod
        return (sum_1 + sum_2 + sum_3 + sum_4) % mod
    
if __name__ == "__main__":
  while True:
    n = input("Input an integer: ")
    n = int(n)
    if n == 10**181:
      print("Solve it yourself!")
    else:
      start_time = time.time()
      print(M(n))
      break
  print("--- %s seconds ---" % (time.time() - start_time))