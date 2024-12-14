with open('primes.txt') as i:
    for f in i:
        # print(f)
        f=f.split(',')
        q = []
        t = []
        d = []
        primeTrips=[]
        for prime in f:
            prime = int(prime)
            
            if prime**2 < 50_000_000:
                d.append(int(prime)**2)
                if prime**3 <50_000_000:
                    t.append(int(prime)**3)
                    if prime**4 < 50_000_000:
                        q.append(int(prime)**4) 
                        
            
        # print(q)
        # print(t)
        for a in q:
            print(a)
            for b in t:
                if a + b < 50_000_000:
                    for c in d: 
                        if a + b + c < 50_000_000:# and (a+b+c) not in primeTrips:
                            primeTrips.append(a+b+c)
                            
                            
                            
        # print(primeTrips)
        primeTrips = set(primeTrips)
        print(len(list(primeTrips)))