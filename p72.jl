#72 counting fractions
#for every number up to 1 million, how many coprime numbers are less than each digit
#use a dict

#coprime sieve

using Primes

function PrimeFacSet(n)
    n < 2 && return Set(Int[])
    facSet = Set{Int}()

    if n % 2 == 0
        facSet = union!(facSet, 2)
        while n % 2 == 0
            n = n ÷ 2
        end
    end

    for i in collect(3:2:floor(Int, sqrt(n)) + 1)
        if n % i == 0
            facSet = union!(facSet, i)
            while n % i == 0
                n = n ÷ i
            end
        end
    end

    if n > 2
        facSet = union!(facSet, n)
    end

    return facSet
end

function euler_totient(n)
    if n == 1
        return 1
    end

    pfs = PrimeFacSet(n)
    result = n

    for p in pfs
        result *= (1 - 1/p)
    end

    return round(Int, result)
end

function count_reduced_fractions(limit)
    total_fractions = 0
    for n in 2:limit
        total_fractions += euler_totient(n)
    end
    return total_fractions
end

limit = 1000000
println("Total number of proper reduced fractions with a denominator under $limit: ", count_reduced_fractions(limit))
