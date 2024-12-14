struct Frac
    numer::BigInt
    denom::BigInt
end

function simpF(f::Frac)
    g = gcd(f.numer, f.denom)
    return Frac(div(f.numer, g), div(f.denom, g))
end

function addFrac(f1::Frac, f2::Frac)
    return simpF(Frac(f1.numer * f2.denom + f2.numer * f1.denom, f1.denom * f2.denom))
end

function invFrac(f::Frac)
    return Frac(f.denom, f.numer)
end

function Base.show(io::IO, f::Frac)
    print(io, f.numer, "/", f.denom)
end

function term(level)
    if level == 1
        return 2
    elseif mod(level, 3) == 0
        return div(level, 3) * 2
    else
        return 1
    end
end

function infF(level)
    if level == 1
        return Frac(term(level), 1)
    end

    return addFrac(Frac(term(level), 1), invFrac(infF(level - 1)))
end

result = infF(100)
println(result)

function sum_of_digits(n::BigInt)
    return sum(parse(Int, digit) for digit in string(n))
end

numerator_sum = sum_of_digits(result.numer)
println(numerator_sum)
