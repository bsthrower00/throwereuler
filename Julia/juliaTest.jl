println("Hello, World!")

function sieve_of_eratosthenes(limit::Int)
    primes = trues(limit)
    primes[1] = false

    for p in 2:isqrt(limit)
        if primes[p]
            for i in p^2:p:limit
                primes[i] = false
            end
        end
    end

    return findall(primes)
end




