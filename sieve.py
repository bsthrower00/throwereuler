def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    
    return [i for i in range(2, n + 1) if primes[i]]

def export_primes_to_file(primes, filename):
    with open(filename, 'w') as file:
        for prime in primes:
            file.write(str(prime) + '\n')

def main():
    n = int(input("Enter the value of n: "))
    primes = sieve_of_eratosthenes(n)
    filename = input("Enter the filename to save the primes to (e.g., primes.txt): ")
    export_primes_to_file(primes, filename)
    print(f"Prime numbers up to {n} have been saved to {filename}")

if __name__ == "__main__":
    main()
